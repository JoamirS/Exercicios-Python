"""
Maria pegou um empréstimo de 1000000 para realizar o pagamento em 5 anos.
A data em que ela pegou o empréstimo foi 20/12/2020 e o vencimento de cada parcela é no dia 20 de cada mês.
- Crie a data do empréstimo 
- Crie a data do final do empréstimo
- Mostre todas as datas de vencimento e o valor de cada parcela
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta

formatted = '%Y/%m/%d %H:%M:%S'

total_loan = 1_000_000
initial_loan_date = datetime.strptime('2020/12/20 00:00:00', formatted)
loan_date = relativedelta(years=5)
# print(final_loan_date)
final_loan = initial_loan_date + loan_date
print(final_loan)

installment_dates_list = []
installment_date = initial_loan_date

while installment_date < final_loan:
    installment_dates_list.append(installment_date)
    installment_date += relativedelta(months=+1)

installment_number = len(installment_dates_list)
installment_value = total_loan / installment_number
    
for date in installment_dates_list:
    print(date.strftime('%d/%m/%Y'), f'R$ {installment_value:,.2f}')
