import streamlit as st
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

#Archivos de uso pandas

df = pd.read_csv("Calidad_del_Agua_Limpio.csv")
df2 = pd.read_csv("contaminantes_mundial.csv", encoding='latin1')

# titulo
st.markdown(
    """
    <h1 style='text-align: center; color: Black; font-family:Times New Roman; font-size:78px;'>
        CALIDAD DEL AGUA
    </h1>
    """,
    unsafe_allow_html=True
)
opcion = st.sidebar.radio("MENU:", ["INICIO", "TABLAS", "GRAFICOS", "NIVEL MUNDIAL","MAPA", "POLITICA_PUBLICA"])
st.markdown(
    """
    <style>
    body {
        background-color: Green;
    }

    .stApp {
        background-color: #E8F8F5;
    }
    </style>
    """,
    unsafe_allow_html=True
)
if opcion == "INICIO":

    st.markdown(
    """
    <h1 style='text-align: center; color: Black; font-family:Bahnschrift; font-size:28px;'>
        ¿Qué Problemática Enfrentamos?
    </h1>
    """,
    unsafe_allow_html=True
    )
    col1, col2 = st.columns([2, 3])

    with col1:
        st.markdown("###   ")
        image = Image.open("riolimpio.jpeg")
        st.image(image, use_container_width=True)
        image2 = Image.open("riosucio.jpeg")
        st.image(image2, use_container_width=True)
        image3 = Image.open("crisis.png")
        st.image(image3, use_container_width=True)
        st.caption("FOTO: CREACIÓN IA")

    with col2:
        st.markdown("####    ")
        texto_intro = """
        <div style='text-align: justify'>
        En México, la crisis ambiental relacionada con la contaminación del agua no es solo un problema ecológico, sino también un dilema económico, jurídico y de política pública. La degradación de los cuerpos de agua superficiales ,ríos, lagos y presas,no solo pone en riesgo la biodiversidad, sino que afecta directamente la economía de las comunidades que dependen de estos recursos para su vida diaria: desde el consumo humano hasta actividades productivas como la agricultura y la pesca. El propio presidente del Banco Mundial, David Malpass (2022), ha alertado sobre el impacto económico de esta situación: "El deterioro de la calidad del agua frena el crecimiento y exacerba la pobreza en muchos países". Desde un enfoque jurídico y de política pública, la situación también representa una violación al derecho humano al agua, al medio ambiente sano y a la salud, todos reconocidos como garantías tanto en la Constitución mexicana como en tratados internacionales firmados por México. A pesar de ello, las prácticas de vertido sin tratamiento, el uso excesivo de agroquímicos y la escasa vigilancia sobre industrias contaminantes continúan siendo comunes. Esto evidencia una desconexión entre la normativa ,como la Norma Oficial Mexicana NOM-127-SSA1-2021, Agua para uso y consumo humano. Límites permisibles de la calidad del agua, y su aplicación real. Este análisis tiene como objetivo principal profundizar en el significado y los efectos que generan tres indicadores críticos de la calidad del agua: la Demanda Bioquímica de Oxígeno (DBO), la Demanda Química de Oxígeno (DQO) y los Sólidos Suspendidos Totales (SST). Posteriormente, se interpretará una base de datos de la CONAGUA para analizar la situación actual de la calidad del agua en México en lo que respecta a estas variables, y se desarrollará una propuesta de política pública orientada a comenzar a enfrentar esta problemática de manera integral.
        </div>
        """
        st.markdown(texto_intro, unsafe_allow_html=True)
    


#MARCO
    st.markdown(
    """
    <h1 style='text-align: center; color: Black; font-family:Bahnschrift; font-size:28px;'>
       Marco Teórico
    </h1>
    """,
    unsafe_allow_html=True
    )
    
    col3, col4 = st.columns([3, 6])
    with col3:
        st.markdown("###   ")
        image = Image.open("contamin.png")
        st.image(image, use_container_width=True)
        image2 = Image.open("ejem.png")
        st.image(image2, use_container_width=True)
        st.caption("FOTO: CREACIÓN IA")

    with col4:
#Desarrollo 1        
        texto_desarrollo1 = """
        <div style='text-align: justify'>
        Gracias a una base de datos publicada por la CONAGUA, pudimos observar que en México una proporción significativa de los cuerpos de agua superficiales ,como ríos, lagos y presas, presenta altos niveles de contaminación, especialmente por parámetros como la Demanda Bioquímica de Oxígeno (DBO), la Demanda Química de Oxígeno (DQO) y los Sólidos Suspendidos Totales (SST). Estas tres variables son clave para evaluar la calidad del agua, ya que reflejan la presencia de materia orgánica, sustancias químicas contaminantes y residuos sólidos. SEMARNAT (2009) justifica la elección de estas variables de la siguiente forma “Mientras tanto, para evaluar la calidad del agua se ha decidido utilizar tres parámetros indicadores de la misma, que muestran la influencia antropogénica desde el punto de vista de la afectación por la presencia de centros urbanos e industriales que por sus características producen desechos líquidos de calidad diferenciable.  Para ello se ha considerado utilizar la Demanda Bioquímica de Oxígeno (DBO5), la Demanda Química de Oxígeno (DQO) y los Sólidos Suspendidos Totales (SST)”. El nivel de contaminación de los cuerpos de agua se identifica de manera sencilla con un semáforo el cual funciona de la siguiente manera según CONAGUA (2023) “El semáforo para agua superficial considera lo siguiente: si uno o más de los siguientes parámetros: DBO5, DQO, ENTEROC_FEC, y/o TOX, incumplen, entonces el semáforo será de color rojo; si los parámetros anteriores cumplen, pero uno o más de los siguientes parámetros: SST, %OD, CF y/o E_COLI, incumplen, el semáforo será amarillo; y, cuando se da el cumplimiento de todos los indicadores, el semáforo será verde”.
        </div>
        """
        st.markdown(texto_desarrollo1, unsafe_allow_html=True)  
    
    
    
    
#Desarrollo 2
    st.markdown(
    """
    <h1 style='text-align: center; color: #E8F8F5; font-family:Bahnschrift; font-size:19px;'>
    --------
    </h1>
    """,
    unsafe_allow_html=True
    )
    texto_desarrollo2 = """
    <div style='text-align: justify'>
    Una alta DBO nos indica que hay una gran cantidad de materia orgánica en el agua, la cual, al descomponerse, consume oxígeno disuelto y termina afectando a la vida acuática. Esto también facilita la proliferación de microorganismos patógenos. La DBO es uno de los indicadores más importantes de contaminación, pues mide cuántas unidades de oxígeno necesitan los microorganismos aerobios para descomponer la materia biodegradable presente en el agua. De acuerdo con la Universidad Nacional Mayor de San Marcos (2014), la DBO se define como “una medida de la cantidad de oxígeno requerido para la oxidación de la materia orgánica biodegradable, presente en la muestra de agua, como resultado de la acción de oxidación aerobia”. Lamentablemente, la Universidad Nacional Mayor de San Marcos (2014) identifica que los cuerpos de agua superficiales como ríos y lagos han sido utilizados históricamente como vertederos naturales, tanto de residuos urbanos como industriales. Esto ha provocado que la contaminación orgánica se traduzca en una disminución del oxígeno disuelto, lo que genera una cadena de consecuencias: desde la alteración del pH hasta la muerte de peces y plantas acuáticas, afectando seriamente la biodiversidad local. El artículo emitido por la Universidad Nacional Mayor de San Marcos (2014) menciona que ya desde el siglo XIX, Dupré observó que existía una relación directa entre la cantidad de oxígeno disuelto y el nivel de contaminación del agua. Esta observación ayudó a consolidar la DBO como un parámetro confiable para medir la actividad biológica y la materia orgánica en cuerpos de agua. Además, la DBO también se utiliza en el establecimiento de Límites Máximos Permisibles (LMP), en la evaluación del desempeño de las Plantas de Tratamiento de Aguas Residuales (PTAR) y en el diseño de sistemas de tratamiento biológico. Por todo esto, un valor elevado de DBO no solo indica un problema ambiental, sino también un riesgo para la salud pública, sobre todo cuando esa agua se usa para consumo humano, riego o recreación. Por otro lado, una alta Demanda Química de Oxígeno (DQO) revela la presencia de contaminantes químicos como detergentes, solventes, residuos industriales o pesticidas. Muchos de estos compuestos son tóxicos, se mantienen en el ambiente por mucho tiempo y se acumulan en los organismos vivos, lo que representa un gran riesgo tanto para la salud humana como para los ecosistemas acuáticos. En este sentido, es clave conocer las características de las aguas residuales antes de tratarlas. Como bien dice Arellano (2011), “la generación de aguas residuales es un producto inevitable de toda actividad humana. Para lograr un tratamiento y disposición final aceptable de éstas, es indispensable conocer sus características físicas, químicas y biológicas; de su significado y de sus efectos principales sobre la fuente receptora”. El problema se agrava cuando estas aguas contaminadas se vierten sin tratamiento, afectando directamente a los cuerpos receptores. Además, hay otras fuentes de contaminación como los residuos agrícolas ,plaguicidas, herbicidas, pesticidas y fertilizantes, que también alteran profundamente la calidad del agua superficial y subterránea. Los Sólidos Suspendidos Totales (SST) también son un gran problema, ya que afectan directamente la calidad del agua. Su presencia reduce la transparencia, dificulta los procesos de potabilización y promueve la propagación de bacterias y parásitos. Como advierte el Water Quality Research Journal (2023), “la contaminación del agua causada por sólidos, incluidas las partículas suspendidas y disueltas, plantea desafíos críticos para la sostenibilidad ambiental, la salud pública y el desarrollo económico”. Altas concentraciones de SST provocan turbidez extrema, impiden el paso de la luz solar y afectan los procesos fotosintéticos necesarios para mantener el equilibrio ecológico. Además, estos sólidos actúan como vectores de otros contaminantes como metales pesados, nutrientes y microorganismos. Esto agrava aún más los efectos negativos, ya que se pueden detonar procesos como la eutrofización y el desarrollo de enfermedades infecciosas.
    </div>
    """
    st.markdown(texto_desarrollo2, unsafe_allow_html=True)  

#Desarrollo 3
    st.markdown(
    """
    <h1 style='text-align: center; color: #E8F8F5; font-family:Bahnschrift; font-size:19px;'>
    --------
    </h1>
    """,
    unsafe_allow_html=True
    )
    col5, col6 = st.columns([3, 6])
    with col5:
        st.markdown("###   ")
        image = Image.open("marco1.png")
        st.image(image, use_container_width=True)
        image2 = Image.open("marco2.png")
        st.image(image2, use_container_width=True)
        st.caption("FOTO: CREACIÓN IA")

    with col6:
        texto_desarrollo3 = """
        <div style='text-align: justify'>
        BBVA (2025) identifica como principales consecuencias del agua contaminada las siguientes: “Es una fuente continua de enfermedades, unas de efectos más rápidos y graves, como el cólera o el tifus, y otras menos evidentes que actúan a más largo plazo produciendo un debilitamiento de la población. Por ello, tanto por motivos de salud pública como de protección del medioambiente, la calidad del agua debería ser el objetivo fundamental de su gestión. Las consecuencias que provocan las aguas contaminadas deberían ser una prioridad para los gobiernos: la desaparición de la biodiversidad y los ecosistemas acuáticos, la alteración de la cadena alimentaria, la aparición de enfermedades por beber o utilizar agua contaminada y la mortalidad infantil, entre otras.” Como podemos leer el agua no solo afecta en temas de salud a las personas sino también a la biodiversidad del país.   Como analizamos en el texto anterior, más allá del daño ambiental, estamos frente a una problemática que afecta la vida diaria de muchas personas. Por eso, atender esta situación debe ser una prioridad para México. No solo por una cuestión de salud y justicia ambiental, sino también porque compromete el cumplimiento de los Objetivos de Desarrollo Sostenible propuestos por la ONU, especialmente el ODS 6 (Agua limpia y saneamiento) y el ODS 3 (Salud y bienestar). Es urgente actuar para proteger tanto nuestros ecosistemas como a las comunidades que dependen de ellos.
        </div>
        """
        st.markdown(texto_desarrollo3, unsafe_allow_html=True)  

#HIPOTESIS
    st.markdown(
    """
    <h1 style='text-align: center; color: #E8F8F5; font-family:Bahnschrift; font-size:19px;'>
    --------
    </h1>
    """,
    unsafe_allow_html=True
    )
    col7, col8 = st.columns([6, 3])
    with col7:
        st.markdown(
    """
    <h1 style='text-align: center; color: Black; font-family:Bahnschrift; font-size:28px;'>
       Hipotesis
    </h1>
    """,
    unsafe_allow_html=True
    )
        texto_hipotesis = """
        <div style='text-align: justify'>
        Si la información sobre la calidad del agua ,específicamente los niveles de DBO, DQO y SST, estuviera disponible de forma clara, rápida y accesible para la ciudadanía, habría una mayor conciencia del problema y presión social para que las autoridades tomen medidas. Esto podría ayudar no solo a reducir los niveles de contaminación en cuerpos de agua, sino también a mejorar la vigilancia, el cumplimiento de la norma y a proteger la salud pública. Una política pública enfocada en acercar estos datos a la gente puede ser el primer paso para enfrentar esta crisis ambiental.
        </div>
        """
        st.markdown(texto_hipotesis, unsafe_allow_html=True)
    
    with col8:
        st.markdown("###   ")
        image = Image.open("marco1.png")
        st.image(image, use_container_width=True)
        image2 = Image.open("marco2.png")
        st.image(image2, use_container_width=True)
        st.caption("FOTO: CREACIÓN IA")


 #MAPA Y VIDEO
    st.markdown("<h2 style='text-align: center; color: Black;'>Multimedia</h2>", unsafe_allow_html=True)
    col9, col10 = st.columns(2)
    with col9:
        st.markdown('<p style="text-align: center; font-family:ADLaM Display;">Dale click al mapa</p>', unsafe_allow_html=True)
        st.markdown("""
            <div style="text-align: center;">
                <a href="https://www.inegi.org.mx/temas/hidrografia/" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/5/5a/Mapa_Ilustrado_de_la_Republica_Mexicana_Publicado_Por_Margaret_M._Crane_Eugenio_Fischgrund.jpg" width="300">
                </a>
            </div>
        """, unsafe_allow_html=True)
    with col10:
        st.markdown('<p style="text-align: center; font-family:ADLaM Display;"> Dale click al video </p>', unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=CgL08UuohAg")
  

#TABLAAAS
elif opcion == "TABLAS":
    st.header("TABLAS")
    st.write("📋")
        
    #Tabla 1
    st.markdown("<h2 style='text-align: center; color: Black;'> 📋 Primeras 10 filas</h2>", unsafe_allow_html=True)
    st.dataframe(df.head(10))

    #Tabla 2
    st.markdown("<h2 style='text-align: center; color: Black;'> 📋 Promedio por Estado (solo columnas seleccionadas)</h2>", unsafe_allow_html=True)
    columnas_seleccionadas = ['ESTADO', 'DBO_mgL', 'DQO_mgL', 'SST_mgL']
    if all(col in df.columns for col in columnas_seleccionadas):
        df_filtrado = df[columnas_seleccionadas]
        promedio_estado = df_filtrado.groupby('ESTADO').mean(numeric_only=True)
        st.dataframe(promedio_estado)

    #Tabla 3
    st.markdown("<h2 style='text-align: center; color: Black;'> 📋 Top 20 valores más altos de DQO por estado</h2>", unsafe_allow_html=True)
    columnas = ['ESTADO', 'DBO_mgL', 'DQO_mgL', 'SST_mgL']
    if all(col in df.columns for col in columnas):
        df_filtrado = df[columnas]
        df_ordenado = df_filtrado.sort_values(by='DQO_mgL', ascending=False).head(20)
        st.dataframe(df_ordenado)

    
if opcion == "GRAFICOS":
    st.markdown(
    """
    <h1 style='text-align: center; color: Black; font-family:Bahnschrift; font-size:28px;'>
        📊 Graficos
    </h1>
    """,
    unsafe_allow_html=True
    )
    #Grafica 1	
    st.markdown("<h2 style='text-align: center; color: Black;'> 📊 Histograma de DQO_mgL</h2>", unsafe_allow_html=True)
    if 'DQO_mgL' in df.columns:
        fig1, ax1 = plt.subplots()
        ax1.hist(df['DQO_mgL'].dropna(), bins=20, color="gray", edgecolor='black' )
        ax1.set_xlabel("DQO (mg/L)")
        ax1.set_ylabel("Números de cuerpos de agua")
        ax1.set_title("Distribución de DQO en Cuerpos de Agua")
        st.pyplot(fig1)
#Grafica2
    st.markdown("<h2 style='text-align: center; color: Black;'> 📊 Distribución del Semáforo de Calidad del Agua en México</h2>", unsafe_allow_html=True)        
    if 'SEMAFOROO' in df.columns:
        conteo = df['SEMAFOROO'].value_counts()
        fig2, ax2 = plt.subplots()
        colores = {'Rojo': 'red', 'Amarillo': 'gold', 'Verde': 'green'}
        ax2.pie(conteo, labels=conteo.index, autopct='%1.1f%%', colors=[colores.get(label, 'gray', ) for label in conteo.index] )
        st.pyplot(fig2)

#Grafica 3
    st.markdown("<h2 style='text-align: center; color: Black;'> 📊 Visualización de cotaminantes</h2>", unsafe_allow_html=True)                
    line_data = df[["DBO_mgL", "DQO_mgL","SST_mgL"]].copy()
    st.line_chart(line_data)
#grafico 4
    st.markdown("<h2 style='text-align: center; color: Black;'> 📊 Estados más contaminados</h2>", unsafe_allow_html=True)                    
    estados_validos = df[~df['ESTADO'].isin(colores)]
    numop=estados_validos['ESTADO'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(numop, labels=numop.index, autopct='%1.1f%%', textprops={'fontsize': 7})
    st.pyplot(fig)



elif opcion == "NIVEL MUNDIAL":
    st.markdown(
    """
    <h1 style='text-align: center; color: Black; font-family:Bahnschrift; font-size:28px;'>
       Estadística De Contaminantes En El Mundo
    </h1>
    """,
    unsafe_allow_html=True
    )
    st.dataframe(df2)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(df2['parametros_code'], df2['porcentaje'], color='purple')
    ax.set_xlabel('Contaminantes (parametros_code)', fontsize=15)
    ax.set_ylabel('Porcentaje', fontsize=15)
    ax.set_title('Porcentaje por Contaminante', fontsize=20)
    plt.xticks(rotation=90)
    st.caption("GRQA water quality parameter statistics. https://essd.copernicus.org/articles/13/5483/2021/#bib1.bibx32")
    st.pyplot(fig)

if opcion == "MAPA":
    df = pd.read_csv("ciudad.csv")
    st.dataframe(df)
    st.markdown('<p style="text-align: center; color: Black; font-family:Times New Roman; font-size:38px">Ubicaciones de cuerpos de agua investigados</p>', unsafe_allow_html=True)
    st.map(df)

elif opcion == "POLITICA_PUBLICA":
    st.markdown(
    """
    <h1 style='text-align: center; color: Black; font-family:Bahnschrift; font-size:28px;'>
       Propuesta De Emprendimiento Publico
    </h1>
    """,
    unsafe_allow_html=True
    )
    col11, col12 = st.columns(2)
    with col11:
        texto_politica = """
        <div style='text-align: justify'>
        Como pudimos observar anteriormente, la contaminación del agua es un fenómeno presente en México y, por razones de salud pública, biodiversidad ecológica y hasta factores económicos, como los analizados en la introducción, es urgente comenzar a tomar acción. Por esta razón, decidimos utilizar la base de datos de la CONAGUA y enfocarnos específicamente en esta problemática.
        Actualmente, un factor clave para el desarrollo de los países es el acceso a la información, y México no es la excepción. Un artículo escrito por Alejandro Calvillo, publicado en la página oficial del Gobierno de México (2024),a pesar de que la información es pública aclara que los mexicanos tienen una fuerte desconfianza en la calidad del agua: “La desconfianza en la calidad del agua entre los mexicanos surgió de eventos reales, como los daños causados por el terremoto de 1985 a la red de distribución de agua potable en la Ciudad de México y la epidemia de cólera en el país en 1991.”
        Aunque esta información sobre la contaminación de los cuerpos de agua sí es pública y se explica con claridad la metodología que se usa para clasificar cada cuerpo de agua mediante un semáforo de colores, es complicado entender qué significan las variables DBO, DQO y SST y por qué son importantes. Además, resulta poco accesible para la mayoría de las personas, ya que la base de datos es pesada de descargar, no tiene un buscador amigable por ubicación y requiere conocimientos técnicos para su interpretación.
        A esto se suma una dificultad aún más actual: la poca atención que los ciudadanos pueden dedicar a este tipo de información si no está presentada de forma clara y rápida. Como señala La Vanguardia (2019), “Uno, dos, tres, cuatro, cinco. El tiempo que se tarda en recitar en voz alta estos cinco números es lo que dura la atención media que los ciudadanos dedican de manera sostenida a un mensaje, un artículo de prensa, una fotografía, un vídeo o una conversación.” Este dato enfatiza que la información debe ser inmediata, digerible y visualmente accesible para poder captar la atención del ciudadano promedio.
        </div>
        """
        st.markdown(texto_politica, unsafe_allow_html=True)
    with col12:
        st.markdown("###   ")
        image = Image.open("politica.png")
        st.image(image, use_container_width=True)
        image2 = Image.open("politica1.png")
        st.image(image2, use_container_width=True)
        image3 = Image.open("politica3.png")
        st.image(image3, use_container_width=True)
        st.caption("FOTO: CREACIÓN IA")
    st.markdown(
    """
    <h1 style='text-align: center; color: #E8F8F5; font-family:Bahnschrift; font-size:19px;'>
    --------
    </h1>
    """,
    unsafe_allow_html=True
    )
    
    texto_politica2 = """
    <div style='text-align: justify'>
    Es por estas razones que decidimos desarrollar una interfaz digital accesible que permita visualizar la información de CONAGUA de forma clara, sencilla y rápida. Aunque esta plataforma aún tiene un amplio potencial de desarrollo, consideramos que este es un primer paso significativo. Somos conscientes de que, muchas veces, cuando se plantea una política pública, se busca resolver todos los problemas al mismo tiempo. Sin embargo, creemos firmemente que sentar las bases adecuadas puede representar una gran contribución desde el inicio.
    Esta política pública se enmarca dentro de lo que se conoce como una iniciativa Civic Tech, la cual, según la Diputación de Jaén (2021), se define como: “El proyecto CIVICTEC tiene como objetivo hacer que la democracia sea más participativa, inclusiva y receptiva mediante la mejora de la participación ciudadana a través de nuevas herramientas y procesos digitales.”
    Siguiendo esta visión, nuestra propuesta busca, a través de herramientas digitales, facilitar el acceso a información técnica y pública ,como la generada por CONAGUA, y convertirla en contenido comprensible para toda la población. El objetivo es empoderar a los ciudadanos mediante el conocimiento, de forma que puedan ejercer una mayor presión y exigencia hacia el gobierno. Esto es fundamental porque, aunque ya existen múltiples regulaciones y normativas que establecen criterios para la calidad del agua, en la práctica los procesos suelen verse afectados por la corrupción, la falta de transparencia y la débil vigilancia institucional sobre el tratamiento de residuos.
    La raíz del problema no está únicamente en la ausencia de leyes, sino en la falta de presión ciudadana informada, la cual permitiría exigir que esas leyes se apliquen de forma efectiva. Si las personas conocen, comprenden y tienen acceso ágil a esta información, estarán en condiciones de exigir mejores decisiones y políticas públicas más eficaces.
    Actualmente, podríamos decir que el gobierno mexicano opera con una racionalidad limitada, concepto propuesto por el economista Herbert A. Simon (1999), quien define esta idea de la siguiente manera:
    “La racionalidad limitada es simplemente la idea de que las decisiones que toman las personas están determinadas no solo por una meta general coherente y por las características del mundo externo, sino también por el conocimiento que los tomadores de decisiones tienen —y no tienen— sobre el mundo, su capacidad o incapacidad para evocar ese conocimiento cuando es relevante, para analizar las consecuencias de sus acciones, para imaginar posibles cursos de acción, para enfrentar la incertidumbre (incluida la incertidumbre que proviene de las posibles respuestas de otros actores), y para decidir entre sus muchos deseos en competencia. La racionalidad está limitada porque estas habilidades están severamente restringidas.”
    </div>
        """
    st.markdown(texto_politica2, unsafe_allow_html=True)
    
    image4 = Image.open("politica2.png")
    st.image(image4, use_container_width=True)
    st.caption("FOTO: CREACIÓN IA")

    texto_politica3 = """
    <div style='text-align: justify'>
    Esto implica que las decisiones gubernamentales no siempre buscan la mejor solución posible, sino una que sea “suficientemente buena” para mantener una apariencia de eficiencia y evitar conflictos sociales. Pero esto solo funciona mientras la población se mantenga poco informada o apática, lo que puede derivar en fenómenos como el groupthink: un pensamiento colectivo acrítico donde se acepta la narrativa oficial sin cuestionamientos, a pesar de que exista una profunda desconfianza respecto a la calidad del agua.
    Lo preocupante es que esa desconfianza, aunque generalizada, carece de fundamentos técnicos o explicaciones claras entre la mayoría de la población. No se sabe con precisión por qué el agua está contaminada, qué lo causa, cuáles son sus efectos, ni mucho menos qué indicadores deben vigilarse. Nuestra interfaz busca revertir esta situación al traducir el lenguaje técnico en información útil, visual y accesible, adecuada a los niveles de comprensión de la ciudadanía en general.
    Creemos que la información clara y útil es la primera línea de defensa frente a la negligencia institucional. Solo una ciudadanía informada puede romper la inercia de la racionalidad limitada y del groupthink para exigir políticas públicas basadas en evidencia y en el interés colectivo.
    Finalmente, y por motivos de profesionalismo, analizaremos el costo-beneficio de esta propuesta. Como se expuso en los argumentos anteriores, esta política pública representa un excelente ejemplo de eficiencia en términos de costo-beneficio, ya que su implementación es relativamente sencilla y, de lograr su objetivo, los beneficios que aportará a la población serán enormes.
    Se trata de una forma efectiva y accesible de potenciar los recursos ya disponibles por parte del gobierno, promoviendo una ciudadanía más informada, participativa y crítica. En resumen, esta política pública ofrece una gran rentabilidad social con una inversión técnica y económica moderada
    </div>
        """
    st.markdown(texto_politica3, unsafe_allow_html=True)
    col13, col14 = st.columns(2)
    with col13:
        texto_politica4 = """
        <div style='text-align: justify'>
        En resumen, la contaminación del agua en México es un problema urgente que no solo afecta la salud pública, el medio ambiente y la economía, sino que también se ve agravado por la falta de información clara y accesible para la ciudadanía. Aunque existen bases de datos oficiales como las de CONAGUA, su formato técnico y difícil acceso limita el poder de acción de las personas, quienes, aunque desconfían del agua, no entienden del todo por qué o cómo pueden actuar.
        Nuestra propuesta de política pública, enmarcada en la lógica de las Civic Tech, busca romper con esa barrera informativa a través de una plataforma digital sencilla, rápida y entendible. No pretendemos resolver todo de golpe, pero sí dar un paso firme en la dirección correcta: empoderar a la población mediante el acceso útil a los datos, algo que el propio gobierno ya tiene, pero que no ha sabido comunicar de forma efectiva.
        Con esto, esperamos no solo informar, sino también activar la participación ciudadana y romper el ciclo de racionalidad limitada en la toma de decisiones públicas. Si las personas saben lo que pasa con el agua que consumen, podrán presionar para que se apliquen correctamente las regulaciones, y con ello contribuir a mejorar el sistema desde la raíz.
        Finalmente, lo más destacable de esta política es que su relación costo-beneficio es altamente favorable. Con una inversión relativamente baja, se pueden lograr grandes cambios en la forma en que la ciudadanía se involucra con los temas ambientales y de salud. Es una propuesta realista, útil y necesaria para construir un México más consciente, más informado y más participativo.
        </div>
        """
        st.markdown(texto_politica4, unsafe_allow_html=True)
    with col14:
        st.markdown("###   ")
        image = Image.open("politica4.png")
        st.image(image, use_container_width=True)
        image2 = Image.open("politica5.png")
        st.image(image2, use_container_width=True)
        st.caption("FOTO: CREACIÓN IA")
    st.markdown(
    """
    <h1 style='text-align: center; color: #E8F8F5; font-family:Bahnschrift; font-size:19px;'>
    --------
    </h1>
    """,
    unsafe_allow_html=True
    )
    
    st.markdown(
    """
    <h1 style='text-align: center; color: Black; font-family:Bahnschrift; font-size:28px;'>
       Referencias
    </h1>
    """,
    unsafe_allow_html=True
    )
    texto_referencias = """
    <div style='text-align: justify; color: #1f4e79; font-family: Times New Roman; font-size: 18px;'>'>
    ALEJANDRO CALVILLO. (2024). La aberración del agua embotellada. Gobierno de México. Recuperado el 10 de junio de 2025, de https://secihti.mx/la-aberracion-del-agua-embotellada/
    BBVA. (2025, 21 mayo). ¿Qué es la contaminación del agua? Causas, tipos y consecuencias. BBVA Noticias. https://www.bbva.com/es/sostenibilidad/la-contaminacion-del-agua-descubre-las-causas-y-consecuencias/
    CONAGUA. (2023). Indicadores de calidad del agua. Gobierno de México. Recuperado el 10 de junio de 2025, de https://www.gob.mx/conagua/es/articulos/indicadores-de-calidad-del-agua?idiom=es
    Denchak, M. (2048). La contaminación del agua: Todo lo que necesitas saber. NRDC. Recuperado el 8 de junio de 2025, de https://www.nrdc.org/es/stories/contaminacion-agua-todo-lo-necesitas-saber
    Gobierno de México. (2025). Agua. Informe del Medio Ambiente. https://apps1.semarnat.gob.mx:8443/dgeia/informe15/tema/cap6.html
    Herbert A. Simon. (1999). Bounded Rationality in Social Science: Today and Tomorrow. Department of Psychology, Carnegie Mellon University, Pittsburgh. Recuperado el 10 de junio de 2025, de https://experiencia21.tec.mx/courses/566369/assignments/19042999?return_to=https%3A%2F%2Fexperiencia21.tec.mx%2Fcalendar%23view_name%3Dmonth%26view_start%3D2025-06-10
    Inclusión ciudadana y cívica y la transformación digital de los procesos de decisión pública – CIVITEC – Fondos Europeos Diputación Provincial de Jaén. (2021). https://fondoseuropeos.dipujaen.es/proyectos/inclusion-ciudadana-y-civica-y-la-transformacion-digital-de-los-procesos-de-decision-publica-civitec/#:~:text=El%20proyecto%20CIVITEC%20tiene%20como%20objetivo%20hacer,participaci%C3%B3n%20p%C3%BAblica%20en%20varios%20niveles%20de%20gobernanza.
    Iberdrola. (2021, 22 abril). Contaminación del agua. Iberdrola. https://www.iberdrola.com/sostenibilidad/contaminacion-del-agua#:~:text=Es%20decir%2C%20es%20agua%20t%C3%B3xica,fiebre%20tifoidea%20y%20la%20poliomielitis.
    Iberdrola. (2025). Contaminación del agua. Recuperado el 8 de junio de 2025, de https://www.iberdrola.com/sostenibilidad/contaminacion-del-agua#:~:text=Los%20principales%20contaminantes%20del%20agua,resulte%20invisible%20en%20muchas%20ocasiones.
    López, F., Fierro, J., & Calero, R. (2015). Disminución de la demanda química de oxígeno (DQO) en aguas residuales generadas en una industria de agroquímicos. Revista Universidad de Guayaquil, 121(3), 63–72. https://doi.org/10.53591/rug.v121i3.392
    Luviano Soto, I., Concha Sánchez, Y., & Raya, A. (2025). Calidad del agua contaminada por sólidos suspendidos totales clasificados mediante un enfoque de redes neuronales artificiales. Water Quality Research Journal, 60(1), 214–228. https://doi.org/10.2166/wqrj.2024.061
    NORMA OFICIAL MEXICANA NOM-127-SSA1-2021, Agua para uso y consumo humano. Límites permisibles de la calidad del agua. (2025). Gobierno de México. https://www.dof.gob.mx/nota_detalle_popup.php?codigo=5650705
    Raffo Lecca, E., & Ruiz Lizama, E. (2014). Caracterización de las aguas residuales y la demanda bioquímica de oxígeno. Industrial Data, 17(1), 71–80. https://www.redalyc.org/pdf/816/81640855010.pdf
    Rodríguez, I. (2022, 1 agosto). Contaminada, 59.1% del agua superficial de México. El Economista. https://www.eleconomista.com.mx/politica/Contaminada-59.1-del-agua-superficial-de-Mexico-20220801-0005.html
    SEMARNAT. (2009). Indicadores de calidad del agua. https://apps1.semarnat.gob.mx:8443/dgeia/compendio_2009/compendio_2009/10.100.8.236_8080/ibi_apps/WFServlet28b9.html
    Vanguardia, L. (2025, 10 junio). Multitudinaria misa de acción de gracias por la declaración de venerable a Antoni Gaudí. La Vanguardia. https://www.lavanguardia.com/vida/20250610/10775004/multitudinaria-misa-accion-gracias-declaracion-venerable-gaudi-sagrada-familia-barcelona-omella.html
    </div>
    """
    st.markdown(texto_referencias, unsafe_allow_html=True)
    
    
