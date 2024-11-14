def get_personal_data(**kwargs):
    print(type(kwargs))
    print(kwargs)
    # print(kwargs['name'])
    # print(kwargs['surname'])
    # print(kwargs['age'])
    # print(kwargs['phone'])


get_personal_data(name='Oleg', surname='Nikitin',age= 15, phone=89174120578)
get_personal_data(surname='Nikitin', phone=89174120578, age= 15)

def planet_space_addres(**kwargs):
    print(kwargs, ' :')
    for key , value in kwargs.items():
        print(key,': ', value)

planet_space_addres(planet='Earth', star='Sun', galaxy='MilkyWay', age=(4.543e9))