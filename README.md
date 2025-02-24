# NaturalLanguageProcessingProyecto
# Proyecto de Procesamiento del Lenguaje Natural (NLP) - Análisis de Entidades Nombradas

## 📋 Descripción

Este proyecto se centra en el desarrollo de un agente especializado en el reconocimiento de entidades nombradas (NER) aplicado a resúmenes médicos. El objetivo es procesar textos no estructurados generados en hospitales, extrayendo información clave y estructurándola en formatos útiles para la administración clínica y el seguimiento de pacientes.

El agente analiza textos médicos y clasifica entidades como:
- **Personas** (nombres de pacientes o médicos)
- **Fechas** (nacimientos, consultas, diagnósticos)
- **Diagnósticos** (enfermedades detectadas)
- **Medicamentos y dosis**

## 🎯 Objetivo

Transformar texto no estructurado en datos organizados y accesibles, facilitando tareas como:
- Automatización del registro clínico
- Seguimiento de tratamientos
- Optimización de la administración hospitalaria

## 💡 Ejemplos de Uso

**Entrada:**
```
Paciente: Laura Rodríguez, nacida el 10 de marzo de 1980. Consulta del 21 de noviembre de 2024. Diagnóstico: gripe común. Se le recetó paracetamol 500 mg, una cada 8 horas.
```

**Salida JSON:**
```json
{
  "nombre": "Laura Rodríguez",
  "fecha_nacimiento": "1980-03-10",
  "fecha_consulta": "2024-11-21",
  "diagnostico": "gripe común",
  "tratamiento": [
    {
      "medicamento": "paracetamol",
      "dosis": "500 mg",
      "frecuencia": "cada 8 horas"
    }
  ]
}
```

## ⚙️ Tecnologías Utilizadas

- Python
- Natural Language Toolkit (NLTK)
- SpaCy
- Expresiones regulares (RegEx)

## 🚀 Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/nlp-medical-ner.git
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd nlp-medical-ner
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## 🏃 Uso

1. Ejecuta el script principal:
   ```bash
   python main.py
   ```
2. Ingresa el texto del resumen médico cuando se solicite.
3. Obtén la salida en formato JSON.

## 📈 Conclusiones

El agente logra extraer y estructurar con precisión la información clave. Para futuras versiones, se recomienda:
- Optimización de la estructura del JSON para asegurar la inclusión de todos los campos relevantes.
- Implementación de un sistema de validación de datos antes de generar la salida.

## ✅ Mejoras Futuras

- Integración con bases de datos para almacenamiento automático.
- Implementación de una interfaz gráfica para usuarios no técnicos.
- Soporte para múltiples idiomas.

## 🙌 Autor

**Abner Maximiliano Lecona Nieves**

Proyecto desarrollado como parte del curso de Ingeniería en Sistemas.

---

¡Gracias por visitar el proyecto! 

