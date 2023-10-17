import CustomerClass as cc
import ServiceClass as sc
import ServiceQuoteClass as sqc

def main():
    name = 'Michael Ho'
    address = '1234 S University Drive'
    number = '971-282-1140'

    make = 'Honda'
    model = 'CRV'
    year = 2018

    parts_charges = float(input('Enter the parts charges: '))
    labor_charges = float(input('Enter the labor charges: '))
    sales_tax = 0.08

    customer_info = cc.Customer(name, address, number)

    car_info = sc.Car(make, model, year)

    service_quote = sqc.ServiceQuote(parts_charges, labor_charges, sales_tax)

    service_quote.tax_charge()

    service_quote.add_charges()

    print('              _         _')
    print("  __   ___.--'_`.     .'_`--.___   __")
    print(" ( _`.'. -   'o` )   ( 'o`   - .`.'_ )")
    print(" _\.'_'      _.-'     `-._      `_`./_")
    print("( \`. )    //\`         '/\\    ( .'/ )")
    print(" \_`-'`---'\\__,       ,__//`---'`-'_/")
    print("  \`        `-\         /-'        '/")
    print("   `                               '   ")
    print('       ***********************')
    print('       * FIX IT FROGGIES Inc *')
    print('       ***********************')
    print('-------------------------------------')
    print(f'Service Quote for {customer_info.get_name()}')
    print(f'Car Information: {car_info.get_year()} {car_info.get_make()} {car_info.get_model()}')
    print('Estimated Parts Charges: $' + format(service_quote.get_pcharges(), ',.2f'))
    print('Estimated Labor Charges: $' + format(service_quote.get_lcharges(), ',.2f'))
    print('Sales Tax: $' + format(service_quote.get_tax_charge(), ',.2f'))
    print(f'Total Charges: $' + format(service_quote.get_total_charges(), ',.2f'))
    print('-------------------------------------')

main()