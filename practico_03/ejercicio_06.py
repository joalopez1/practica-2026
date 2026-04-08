"""Magic Methods"""

from __future__ import annotations
from typing import List


# NO MODIFICAR - INICIO
class Article:
    """Agregar los métodos que sean necesarios para que los test funcionen.
    Hint: los métodos necesarios son todos magic methods
    Referencia: https://docs.python.org/3/reference/datamodel.html#basic-customization
    """

    def __init__(self, name: str) -> None:
        self.name = name

    # NO MODIFICAR - FIN

    def __repr__(self) -> str:
        return f"'{self.name}'"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Article):
            return NotImplemented
        return self.name == other.name


# NO MODIFICAR - INICIO
class ShoppingCart:
    """Agregar los métodos que sean necesarios para que los test funcionen.
    Hint: los métodos necesarios son todos magic methods
    Referencia: https://docs.python.org/3/reference/datamodel.html#basic-customization
    """

    def __init__(self, articles: List[Article] = None) -> None:
        if articles is None:
            self.articles = []
        else:
            self.articles = articles

    def add(self, article: Article) -> ShoppingCart:
        self.articles.append(article)
        return self

    def remove(self, remove_article: Article) -> ShoppingCart:
        new_articles = []

        for article in self.articles:
            if article != remove_article:
                new_articles.append(article)

        self.articles = new_articles

        return self

    # NO MODIFICAR - FIN
    
    def __str__(self) -> str:
        """
        Se llama al usar str(objeto). Devuelve la representación en string
        de la lista de artículos. __repr__ de Article se encarga del formato.
        """
        return str(self.articles)

    def __repr__(self) -> str:
        """
        Representación oficial para recrear el objeto.
        """
        return f"ShoppingCart({self.articles})"

    def __eq__(self, other: object) -> bool:
        """
        Se llama al usar ==. Comparamos si los dos carritos tienen los mismos
        artículos, sin importar el orden. Usar sets es ideal para esto.
        """
        if not isinstance(other, ShoppingCart):
            return NotImplemented
        # Comparamos los nombres de los artículos para la igualdad
        return set(a.name for a in self.articles) == set(a.name for a in other.articles)

    def __add__(self, other: ShoppingCart) -> ShoppingCart:
        """
        Se llama al usar +. Crea un nuevo carrito con los artículos de ambos.
        """
        if not isinstance(other, ShoppingCart):
            return NotImplemented
        return ShoppingCart(self.articles + other.articles)

# NO MODIFICAR - FIN

manzana = Article("Manzana")
pera = Article("Pera")
tv = Article("Television")

# Test de conversión a String
assert str(ShoppingCart().add(manzana).add(pera)) == "['Manzana', 'Pera']"

# Test de reproducibilidad
carrito = ShoppingCart().add(manzana).add(pera)
assert carrito == eval(repr(carrito))

# Test de igualdad
assert ShoppingCart().add(manzana) == ShoppingCart().add(manzana)

# Test de remover objeto
assert ShoppingCart().add(tv).add(pera).remove(tv) == ShoppingCart().add(pera)

# Test de igualdad con distinto orden
assert ShoppingCart().add(tv).add(pera) == ShoppingCart().add(pera).add(tv)

# Test de suma
combinado = ShoppingCart().add(manzana) + ShoppingCart().add(pera)
assert combinado == ShoppingCart().add(manzana).add(pera)

# NO MODIFICAR - FIN
