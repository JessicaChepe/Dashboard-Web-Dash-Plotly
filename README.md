# Desarrollo de un Dashboard Web usando Dash Plotly

En este repositorio, encontrarás el desarrollo de un panel web utilizando Dash de Plotly con datos en formato CSV. La información utilizada corresponde a las ventas de talleres de arte de un negocio llamado TLBA.

## Introducción a Dash

Dash es un framework de Python para crear aplicaciones web analíticas. Es ideal para aquellos que trabajan con análisis de datos, exploración de datos, visualización, modelado, control de instrumentos e informes.

Está construido sobre Flask, Plotly.js, React y React Js, permitiendo la creación de tableros utilizando Python puro. Dash es de código abierto y sus aplicaciones se ejecutan en el navegador web. Cada aspecto visual de la aplicación es altamente personalizable, incluyendo colores, tamaños, posicionamiento y fuentes.

☝️ A continuación, se presenta un ejemplo de una aplicación Dash que muestra la tasa de fertilidad y la esperanza de vida:

![dash](https://github.com/JessicaChepe/Dashboard-Web-Dash-Plotly/assets/104339906/efdb2242-9223-4e67-8717-a389b81aedff)

🤝 Una aplicación Dash típicamente consta de tres elementos principales:

  1. Componentes Dash: como controles deslizantes, casillas de verificación y menús desplegables para proporcionar interactividad a la aplicación.
  2. Gráficos Plotly: para visualizar los datos de manera efectiva.
  3. Callback: un elemento crítico que conecta los componentes Dash y los gráficos Plotly para crear interactividad. Define cómo los componentes y gráficos interactúan entre sí.

Dash ofrece clases HTML que permiten generar contenido HTML con Python. Para utilizar estas clases, se necesitan importar dash_core_components y dash_html_components.

Se utiliza la clase Div de dash_html_components para crear un contenedor HTML Div, mientras que las etiquetas HTML como H1, H2, etc., se generan con los componentes HTML. Además, dash_html_components incluye todas las etiquetas HTML.

Para añadir gráficos a nuestro diseño, empleamos la clase Graph de dash_core_components. Graph permite visualizaciones interactivas de datos utilizando plotly.js. Esta clase espera un objeto de figura que contenga los datos y los detalles del diseño que se van a trazar. 

👉 Para obtener más información sobre Plotly, visita el siguiente enlace: [Plotly](https://plotly.com/?_gl=1*xjwwia*_ga*MTg2ODU2NzA4NS4xNzExMzA3NDgz*_ga_6G7EE0JNSC*MTcxMTMwNzQ4Mi4xLjAuMTcxMTMwNzQ4Mi42MC4wLjA).

## Explicación del Panel Web

Este repositorio contiene el desarrollo de un panel web utilizando Dash, basado en los siguientes datos detallados en la lista:

📝 Datos:
  * Nombre
  * Abono
  * Distrito
  * Modalidad
  * Mes
  * Año
  * Fecha
  * Edad del Alumno
  * Pago
  * Niños
  * Adolescentes
  * Adultos
  * Sedes (sede 1, 2 y 3)
  * Talleres

Estos datos fueron recopilados del negocio, por lo que no son datos reales y, por motivos de privacidad, no se proporcionará más información. El negocio se dedica a la venta de talleres de arte, y el panel web muestra gráficamente la información recopilada desde el año 2019 hasta 2023.

Referencia:
  * https://aiplanet.com/learn/data-visualization-with-plotly-and-dash-es/crear-aplicaciones-de-dashboard-usando-dash/1645/introduccion-a-dash-diseno-de-una-aplicacion-dash-y-principales-componentes


