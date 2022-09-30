from ast import match_case


def http_error(status):
    match status:
        case 400:
            return "solicitud incorrecta"
        case 404:
            return "no encontrado"
        case 418:
            return "soy una tetera"
        case _:
            return "algo anda mal"
print(http_error(404))
