# Proyecto Swag Labs


*En este proyecto automatice el acceso del usuario de la pagina web Swag Labs, ademas de agregar productos al carrito, llenar el formulario de checkout y finalizar la compra.

**Es necesario importar selenium y webdriver para poder realizar la automatizacion. Dentro de cada archivo importe otros soportes requeridos adicionalmente a selenium, dependiendo de las necesidades de cada prueba.**

## El proyecto Swag Labs cuenta con tres archivos:

1. Data.py, este archivo cuenta con los datos necesarios para realizar la automatizacion.

    1. El URL de la pagina web.
    2. Las variantes del username 
    3. La variante nombre del password 
    4. La variante de la firstname
    5. La variante de la lastname
    6. La variante de postal code

2. Main.py, en este archivo se encuentra:

    i. Las importaciones necesarias son las siguientes:

       `from selenium.webdriver.common.by import By` Esta importacion es necesaria parala busqueda de los elementos.

       `from selenium.webdriver.support import expected_conditions` Esta importacion es necesaria para saber que es lo que se esta esperando en el metodo `Explicit Wait`

       `from selenium.webdriver.support.wait import WebDriverWait` Esta importacion es necesaria para la pagina web espere y se ejecute el metodo `Explicit Wait`.

    ii. El metodo  `Explicit Wait` se encuentra en aquellas clases donde se cambian de pantalla y por lo tanto es necesario un poco mas de tiempo para encontrar el elemento solicitado.

    iii. Todas las clases tienen como primer metodo __int__ para establecer el Driver.

    iv. Cada clase contiene los localizadores necesarios para ubicar dichos elementos en la pagina y poder realizar las interacciones con funciones. Para la ejecucion de las pruebas se utilizan los metodos para hacer Clic, Explicit Wait, Self. Driver entre otros.

**Listado de las Clases:**

    * class Login
    * class AddProducts
    * class ShoppingCart
    * class CheckoutInfo
    * class FinishShopping

3. Test_swag_labs.py, en este archivo se ejecutan la pruebas de automatizazon para crear y acceder a una cuenta en la web de BugBank.
  Las importaciones necesarias para ejecutar las pruebas son:
    *import time
    *import data
    *import main
    *from selenium import webdriver

  Comenzamos con el metodo de clase @classmethod y el metodo setup_class(cls) declarando a clase como un argumento y controlando el driver.  En este caso Chrome.

**Listado de las Test:**

    * def test_login(self): agrega los datos para el acceso del usuario a la cuenta
    * def test_add_product(self): agrega los productos al carrito
    * def test_shopping_cart(self): procede al checkout de la compra
    * def test_checkout_info(self): llena el formulario de envio
    * def test_finish_shopping(self): finaliza la compra

 Por ultimo el metodo teardown_class() finaliza las pruebas cerrando el navegador y detiene el driver.
 
 ## Conclusión del Proyecto Swag Labs
En el proyecto Swag Labs, se automatizó el acceso de usuarios, la adición de productos al carrito, el llenado del formulario de checkout y la finalización de compras utilizando Selenium y WebDriver.

El proyecto incluye tres archivos: Data.py para datos necesarios, Main.py para la lógica de automatización y Test_swag_labs.py para ejecutar las pruebas. Cada clase aborda un aspecto específico del proceso, asegurando la funcionalidad de la página.

El uso de métodos como setup_class y teardown_class permite una gestión eficiente del entorno de prueba. Este proyecto demuestra la efectividad de la automatización en la mejora de la experiencia de compra en Swag Labs.


## Muchas gracias!!!
### Georgina Khamisso
