import openpyxl

book = openpyxl.Workbook()

book.create_sheet('Computadores')

computadores_page = book['Computadores']
computadores_page.append(['Eletrônica','Memória RAM','Preço'])
computadores_page.append(['Computador 1', '8gb RAM', 'R$2500'])
computadores_page.append(['Computador 2', '16gb RAM', 'R$5500'])
computadores_page.append(['Computador 3', '32gb RAM', 'R$8500'])

book.save('Meus Computadores.xlsx')