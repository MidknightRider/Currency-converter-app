import gooeypie as gp
import main as cc

app = gp.GooeyPieApp('Currency Converter')

currency = cc.show_currencies("https://api.exchangerate-api.com/v4/latest/USD")
currency = list(currency.keys())

convert_from_dd = gp.Dropdown(app, currency)
convert_from_dd.selected_index = 0
convert_from_dd.width = 10

convert_to_dd = gp.Dropdown(app, currency)
convert_to_dd.selected_index = 0
convert_to_dd.width = 10


def say_converted(event):
    converted_lbl.text = cc.output(convert_from_dd.selected, convert_to_dd.selected, 1)


convert_btn = gp.Button(app, 'Convert', say_converted)

to_lbl = gp.Label(app, 'to')
converted_lbl = gp.Label(app, '')

app.set_grid(5, 5)
app.add(convert_from_dd, 1, 1, align='center')
app.add(to_lbl, 1, 2, align='center')
app.add(convert_to_dd, 1, 3, align='center')
app.add(convert_btn, 2, 2, align='center')
app.add(converted_lbl, 4, 1, align='center', column_span=3)

app.run()
