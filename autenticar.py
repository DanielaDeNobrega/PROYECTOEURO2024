from purchase import Purchase

def get_receipt_id():
    """Se solicita al cliente el código único de la factura.

    Returns:
        int: Código de la factura.
    """    
    while True: 
        try: 
            receipt_id = int(input("\n\nIngrese el código único de su factura:   "))
            break
        
        except: 
                print("Ingrese un ID válido")
    
    return receipt_id


def validacion(lista_purchases, receipt_id, boletos_validados):
    """Valida el ticket y devuelve un bool

    Args:
        lista_purchases(list): lista de objetos Purchase
        receipt_id (int): el código de la factura.
        boletos_validados (_type_): _description_

    Returns:
        booleano: True sies valido, False si es falso. 
    """    
    codes = []
    for p in lista_purchases: 
        codes.append(Purchase.get_code(p))

    if  receipt_id not in codes: 
        return False
    
    if receipt_id not in boletos_validados: 
        return True
    else: 
        return False


    
