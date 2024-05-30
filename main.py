


class InventarioDomestic:
  def __init__(self, nome, area, description, model, dataOfOrder, valueOfOrder, numberOfSeries) -> None:
    self.nome = nome
    self.area = area
    self.description = description
    self.model = model
    self.dataOfOrder = dataOfOrder
    self.valueOfOrder = valueOfOrder
    self.numberOfSeries = numberOfSeries
  def layout_():
    # Está primeira etapa é onde o usuario digita as informações necessarias para o novo cadastro
    nome = input("Digite o nome do item: ")
    area = input("Digite qual a área este item está localizado: ")
    description = input("Diga um pouco mais sobre este produto: ")
    model = input("Digite qual o modelo do item: ")
    dataOfOrder = input("Qual a data de compra deste produto: ")
    valueOfOrder = input("Qual valor da compra: ")
    numberOfSeries = input("Número de série: ")

    try:
      valueOfOrder = float(valueOfOrder)
    except ValueError:
      print("Valor não valido");
      return None;

    return InventarioDomestic(nome, area, description, model, dataOfOrder, valueOfOrder, numberOfSeries)
  def add_item(nome, area, description, model, dataOfOrder, valueOfOrder, numberOfSeries):
    
    pass