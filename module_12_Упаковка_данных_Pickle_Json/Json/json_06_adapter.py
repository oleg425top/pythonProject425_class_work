import json


class Figure:
    def __init__(self, title, form, color):
        self.title = title
        self.form = form
        self.color = color

    def __str__(self):
        return f" Figure: {self.title}, {repr(self.form)}, {repr(self.color)}"


class Form:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Form:{self.name}'


class Color:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Color:{self.name}>'


class JsonDataAdapter:
    @staticmethod
    def to_json(obj):
        if isinstance(obj, Figure):
            return json.dumps({
                'title': obj.title,
                'form': obj.form.name,
                'color':obj.color.name
            })

    @staticmethod
    def from_json(obj):
        obj = json.loads(obj)

        try:
            form = Form(obj['form']),
            color = Color(obj['color'])
            figure = Figure(obj['title'], form, color)
            return figure
        except AttributeError:
            print('неверная структура')

black = Color('black')
yellow = Color('yellow')
red = Color('red')

rounded = Form('rounded')
squared = Form('squared')
figure_1 = Figure('Black_square', form=squared, color=black)
figure_2 = Figure('Yelow_circle', form=rounded, color=red)
print(figure_1)
print(figure_2)
json_square = JsonDataAdapter.to_json(figure_1)
json_circle = JsonDataAdapter.to_json(figure_2)
print(json_circle)
print(json_square)

square_obj = JsonDataAdapter.from_json(json_square)
circle_obj = JsonDataAdapter.from_json(json_circle)

print(square_obj)
print(circle_obj)