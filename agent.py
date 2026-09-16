#!/usr/bin/env python3
"""
Agente conversacional para el modelo Horn Torus ICC.

Usa la API de Claude (Opus) con tool-use: el modelo interpreta resultados
de un SCL-90-R en lenguaje natural, los convierte en los 12 puntajes
normalizados, y llama a las herramientas que envuelven a HornTorusICC
(horn_torus_experimental.py) para generar el resumen, los graficos y las
exportaciones.

Requiere la variable de entorno ANTHROPIC_API_KEY (nunca la pidas ni la
escribas en este archivo - se lee del entorno).

Uso:
    pip install -r requirements.txt
    export ANTHROPIC_API_KEY=sk-ant-...   (o set en Windows)
    python agent.py
"""

import json

from anthropic import Anthropic

from horn_torus_experimental import HornTorusICC

MODEL = "claude-opus-5"

client = Anthropic()  # lee ANTHROPIC_API_KEY del entorno

# Estado de la sesion: el modelo actualmente cargado (si hay uno)
state = {"model": None}


# ----------------------------------------------------------------------
# Funciones que implementan cada tool
# ----------------------------------------------------------------------
def tool_set_scl90r_scores(**scores):
    state["model"] = HornTorusICC(scores)
    return {"ok": True, "message": "Modelo Horn Torus ICC creado con los puntajes dados."}


def tool_get_model_summary(**_kwargs):
    if state["model"] is None:
        return {"error": "Todavia no hay puntajes cargados. Llama primero a set_scl90r_scores."}
    return {"summary": state["model"].generate_model_summary_text()}


def tool_generate_static_plot(deformed=False, filename=None, **_kwargs):
    if state["model"] is None:
        return {"error": "Todavia no hay puntajes cargados. Llama primero a set_scl90r_scores."}
    filename = filename or ("mi_modelo_deformado.png" if deformed else "mi_modelo.png")
    if deformed:
        state["model"].plot_deformed(save_path=filename, show=False)
    else:
        state["model"].plot_3d(save_path=filename, show=False)
    return {"ok": True, "file": filename}


def tool_save_interactive_html(filename="mi_visualizacion.html", deformed=False, **_kwargs):
    if state["model"] is None:
        return {"error": "Todavia no hay puntajes cargados. Llama primero a set_scl90r_scores."}
    state["model"].save_to_html(filename, deformed=deformed)
    return {"ok": True, "file": filename}


def tool_export_json(filename="mis_datos.json", **_kwargs):
    if state["model"] is None:
        return {"error": "Todavia no hay puntajes cargados. Llama primero a set_scl90r_scores."}
    state["model"].export_to_json(filename)
    return {"ok": True, "file": filename}


TOOL_IMPLEMENTATIONS = {
    "set_scl90r_scores": tool_set_scl90r_scores,
    "get_model_summary": tool_get_model_summary,
    "generate_static_plot": tool_generate_static_plot,
    "save_interactive_html": tool_save_interactive_html,
    "export_json": tool_export_json,
}


# ----------------------------------------------------------------------
# Definiciones de tools (JSON Schema) para la API de Claude
# ----------------------------------------------------------------------
SCL90R_PROPERTIES = {
    "Somatizacion": {"type": "number", "description": "0.0-1.0"},
    "Obsesion-Compulsion": {"type": "number", "description": "0.0-1.0"},
    "Sensibilidad Interpersonal": {"type": "number", "description": "0.0-1.0"},
    "Depresion": {"type": "number", "description": "0.0-1.0"},
    "Ansiedad": {"type": "number", "description": "0.0-1.0"},
    "Hostilidad": {"type": "number", "description": "0.0-1.0"},
    "Ansiedad Fobica": {"type": "number", "description": "0.0-1.0"},
    "Ideacion Paranoide": {"type": "number", "description": "0.0-1.0"},
    "Psicoticismo": {"type": "number", "description": "0.0-1.0"},
    "GSI": {"type": "number", "description": "Global Severity Index, 0.0-1.0"},
    "PST": {"type": "number", "description": "Positive Symptom Total, 0.0-1.0"},
    "PSDI": {"type": "number", "description": "Positive Symptom Distress Index, 0.0-1.0"},
}

TOOLS = [
    {
        "name": "set_scl90r_scores",
        "description": (
            "Crea o reemplaza el modelo Horn Torus ICC con los 12 puntajes normalizados "
            "(0.0-1.0) del SCL-90-R. Llamala en cuanto tengas los 12 valores, aunque sean "
            "estimados a partir de una descripcion en lenguaje natural."
        ),
        "input_schema": {
            "type": "object",
            "properties": SCL90R_PROPERTIES,
            "required": list(SCL90R_PROPERTIES.keys()),
        },
    },
    {
        "name": "get_model_summary",
        "description": "Devuelve el resumen clinico-topologico completo del modelo cargado (curvas S/I/Sigma, metricas ICC, diagnostico estructural).",
        "input_schema": {"type": "object", "properties": {}},
    },
    {
        "name": "generate_static_plot",
        "description": "Genera y guarda una imagen PNG estatica del Horn Torus (estandar o deformado por sintoma).",
        "input_schema": {
            "type": "object",
            "properties": {
                "deformed": {"type": "boolean", "description": "true para el manifold deformado por el SCL-90-R"},
                "filename": {"type": "string", "description": "nombre de archivo de salida (opcional)"},
            },
        },
    },
    {
        "name": "save_interactive_html",
        "description": "Genera y guarda una visualizacion 3D interactiva (Plotly) como archivo HTML standalone.",
        "input_schema": {
            "type": "object",
            "properties": {
                "filename": {"type": "string"},
                "deformed": {"type": "boolean"},
            },
        },
    },
    {
        "name": "export_json",
        "description": "Exporta los puntajes SCL-90-R, coordenadas lacanianas y metricas topologicas a un archivo JSON.",
        "input_schema": {
            "type": "object",
            "properties": {"filename": {"type": "string"}},
        },
    },
]

SYSTEM_PROMPT = """Sos un asistente que ayuda a explorar resultados del SCL-90-R (Derogatis)
a traves del modelo Horn Torus ICC: una metafora topologica lacaniana (NO un instrumento
diagnostico validado clinicamente) que mapea los subindices del test a curvas S
(Significante), I (Imagen del cuerpo), Hilo Pulsional (Trieb) y Sigma (Sintoma) sobre
un horn torus, con un punto de fantasia como foco de angustia maxima.

Cuando el usuario te describa resultados de un SCL-90-R (en texto libre, con numeros
o con descripciones cualitativas), estima los 12 valores normalizados (0.0-1.0) y
llama a set_scl90r_scores. Despues, segun lo que pida el usuario, usa get_model_summary,
generate_static_plot, save_interactive_html o export_json.

Aclara siempre, la primera vez que uses el modelo en una conversacion, que esto es una
herramienta exploratoria/teorica para acompañar la lectura clinica, no un diagnostico
ni un reemplazo del juicio profesional."""


# ----------------------------------------------------------------------
# Loop de conversacion con manejo de tool-use
# ----------------------------------------------------------------------
def run_tool(name, tool_input):
    fn = TOOL_IMPLEMENTATIONS.get(name)
    if fn is None:
        return {"error": f"Tool desconocida: {name}"}
    try:
        return fn(**tool_input)
    except Exception as exc:  # noqa: BLE001 - se reporta al modelo, no se cuelga el loop
        return {"error": str(exc)}


def chat_loop():
    print("Horn Torus ICC Agent (Opus). Escribi 'salir' para terminar.\n")
    messages = []

    while True:
        user_input = input("Vos: ").strip()
        if user_input.lower() in ("salir", "exit", "quit"):
            break
        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})

        while True:
            response = client.messages.create(
                model=MODEL,
                max_tokens=2048,
                system=SYSTEM_PROMPT,
                tools=TOOLS,
                messages=messages,
            )
            messages.append({"role": "assistant", "content": response.content})

            tool_uses = [block for block in response.content if block.type == "tool_use"]

            for block in response.content:
                if block.type == "text" and block.text.strip():
                    print(f"Agente: {block.text}\n")

            if not tool_uses:
                break

            tool_results = []
            for tu in tool_uses:
                result = run_tool(tu.name, tu.input)
                print(f"  [tool] {tu.name}({tu.input}) -> {result}")
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": tu.id,
                    "content": json.dumps(result, ensure_ascii=False),
                })
            messages.append({"role": "user", "content": tool_results})


if __name__ == "__main__":
    chat_loop()
