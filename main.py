import sqlite3
import json
from speak import Voicing
try:
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
      confirm = input("Deseja confirmar os dados? (Y / N): ")

      try:
        valueOfOrder = float(valueOfOrder)
      except ValueError:
        Voicing.sayText("Valor não valido");
        return None;

      return InventarioDomestic(nome, area, description, model, dataOfOrder, valueOfOrder, numberOfSeries)
    def add_item(nome, area, description, model, dataOfOrder, valueOfOrder, numberOfSeries):
      # active = InventarioDomestic.layout_();
      # # Cria um conexão com o banco.
      datas = InventarioDomestic.layout_()
      connectDataBase = sqlite3.connect('database.db');

      # Permite a execução de comando sql no banco
      cur = connectDataBase.cursor()

      cur.execute(f"CREATE TABLE item({datas.nome}, {datas.area}, {datas.description})")
      res = cur.execute("SELECT * FROM item");
      print(res.fetchall())
      exit()

    def acesse_db():
      connectToDb = sqlite3.connect('database.db');
      curs = connectToDb.cursor()

      dataInformation = curs.execute('SELECT * FROM item')
      print(dataInformation.fetchall())

  msg = """
  1) Criar novo item
  2) Ler itens no banco de dados
  3) Atualizar item
  4) Deletar item
  """

  print(msg)
  opt = str(input("Digite umas das opções acima: "))
  if '1' in opt:
    Voicing.sayText("Iniciando cadastro de um novo item!")
    layout = InventarioDomestic.layout_()
    activeFunction = InventarioDomestic.add_item(layout.nome, layout.area, layout.description, layout.model, layout.dataOfOrder, layout.valueOfOrder, layout.numberOfSeries);
    Voicing.sayText("Produto adicionado com sucesso")
except Exception as Exception:
  Voicing.sayText("Ouve um erro no código")
  print(Exception)