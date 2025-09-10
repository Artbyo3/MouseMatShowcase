# MouseMat Showcase

Un sitio web estático moderno para mostrar productos de mouse pads, construido con Flask siguiendo las mejores prácticas.

## 🚀 Características

- **Framework**: Flask con patrón Application Factory
- **Frontend**: Tailwind CSS 4 + CSS personalizado
- **Responsive**: Diseño completamente adaptable con utility-first CSS
- **SEO Friendly**: Meta tags optimizados
- **Manejo de errores**: Páginas 404 y 500 personalizadas
- **Estructura modular**: Separación clara de responsabilidades
- **Build System**: Tailwind CLI para compilación automática

## 📁 Estructura del Proyecto

```
MouseMatShowcase/
├── app.py                 # Aplicación Flask principal
├── requirements.txt       # Dependencias del proyecto
├── .gitignore            # Archivos a ignorar en Git
├── README.md             # Este archivo
├── .venv/                # Entorno virtual (no incluido en Git)
├── static/               # Archivos estáticos
│   ├── css/
│   │   ├── input.css     # Archivo de entrada para Tailwind
│   │   ├── output.css    # CSS compilado por Tailwind
│   │   └── style.css     # Estilos personalizados adicionales
│   ├── js/
│   │   └── main.js       # JavaScript personalizado
│   └── images/           # Imágenes del sitio
└── templates/            # Templates HTML
    ├── base.html         # Template base
    ├── index.html        # Página principal
    ├── about.html        # Página Acerca de
    ├── contact.html      # Página de contacto
    ├── 404.html          # Página de error 404
    └── 500.html          # Página de error 500
```

## 🛠️ Instalación y Configuración

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Node.js 16 o superior
- npm (gestor de paquetes de Node.js)

### Pasos de instalación

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd MouseMatShowcase
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv .venv
   ```

3. **Activar entorno virtual**
   
   **Windows:**
   ```bash
   .venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   source .venv/bin/activate
   ```

4. **Instalar dependencias de Python**
   ```bash
   pip install -r requirements.txt
   ```

5. **Instalar dependencias de Node.js**
   ```bash
   npm install
   ```

6. **Compilar CSS con Tailwind**
   ```bash
   npm run build-css
   ```

7. **Ejecutar la aplicación**
   ```bash
   python app.py
   ```

8. **Abrir en el navegador**
   ```
   http://localhost:5000
   ```

### Comandos de desarrollo

- **Compilar CSS una vez**: `npm run build-css`
- **Compilar CSS en modo watch**: `npm run watch-css`

## 🎨 Personalización

### Agregar nuevas páginas

1. Crear el template HTML en `templates/`
2. Agregar la ruta en `app.py`:
   ```python
   @app.route('/nueva-pagina')
   def nueva_pagina():
       return render_template('nueva_pagina.html')
   ```

### Modificar estilos

- **Tailwind CSS**: Usar clases utility en los templates HTML
- **CSS personalizado**: Editar `static/css/style.css` para estilos adicionales
- **Compilar cambios**: Ejecutar `npm run build-css` después de modificar `input.css`
- **Modo desarrollo**: Usar `npm run watch-css` para compilación automática

### Agregar funcionalidad JavaScript

- Editar `static/js/main.js` para funcionalidad global
- Usar `{% block extra_js %}` en templates para scripts específicos

## 📱 Páginas Incluidas

- **Inicio** (`/`): Página principal con productos destacados
- **Acerca de** (`/about`): Información sobre la empresa
- **Contacto** (`/contact`): Formulario de contacto y información
- **404**: Página de error para URLs no encontradas
- **500**: Página de error para errores del servidor

## 🔧 Configuración de Producción

### Variables de entorno

Crear un archivo `.env` con:
```
FLASK_ENV=production
SECRET_KEY=tu-clave-secreta-muy-segura
FLASK_DEBUG=False
```


## 🎯 Mejores Prácticas Implementadas

- **Application Factory Pattern**: Para mejor organización del código
- **Separación de responsabilidades**: Templates, estáticos y lógica separados
- **Manejo de errores**: Páginas de error personalizadas
- **SEO**: Meta tags y estructura semántica
- **Responsive Design**: Compatible con todos los dispositivos
- **Seguridad**: Configuración de secretos por variables de entorno
- **Mantenibilidad**: Código limpio y bien documentado

## 📝 Próximas Mejoras

- [ ] Integración con base de datos
- [ ] Sistema de autenticación
- [ ] Carrito de compras
- [ ] Panel de administración
- [ ] Integración con APIs de pago
- [ ] Sistema de reviews
- [ ] Búsqueda de productos
- [ ] Newsletter

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Soporte

Si tienes preguntas o necesitas ayuda, no dudes en contactarnos:

- Email: info@mousematshowcase.com
- Teléfono: +1 (555) 123-4567

---

**¡Gracias por usar MouseMat Showcase!** 🎮
