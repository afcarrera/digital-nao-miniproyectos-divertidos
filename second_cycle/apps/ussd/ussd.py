from apps.ussd.option import USSDOption

class USSD(object):
    def __init__(self) -> None:
        self.root = dict()
        self.ids = dict()
        self.actual_package = None
        self.actual_balance = 0
        self.packages = set()
        self.balances = set()
        self.promo_media = '10 GB Solo redes sociales'
        self.promo_media_gb = '10 GB: 5 GB + 5 GB redes'
        self.ids['*123#'] = 0
        self.ids['*100#'] = 12
        self.root[-1] = USSDOption('Regresar', None, None, None, None, None)
        self.root[0] = USSDOption('Menu *123#', None, None, [1,2], None, None)
        self.root[1] = USSDOption('Recargar Saldo', None, 0, [3,4,5,6,-1], None, None)
        self.root[2] = USSDOption('Activar paquete (Se reemplazará si hay un paquete activo)', None, 0, [7,8,9,-1], None, None)
        self.root[3] = USSDOption('5 USD', self.charge_balance('5',3), 1, [-1], 5, None)
        self.root[4] = USSDOption('10 USD', self.charge_balance('10',4), 1, [-1], 10, None)
        self.root[5] = USSDOption('20 USD', self.charge_balance('20',5), 1, [-1], 20, None)
        self.root[6] = USSDOption('30 USD', self.charge_balance('30',6), 1, [-1],30, None)
        self.root[7] = USSDOption('10 GB x 10 USD', None, 2, [10,11,-1], 10, None)
        self.root[8] = USSDOption('20 GB x 20 USD', self.activate_package('20',8), 2, [-1], 20, None)
        self.root[9] = USSDOption('30 GB x 30 USD', self.activate_package('30',9), 2, [-1], 30, None)
        self.root[10] = USSDOption(self.promo_media, self.activate_package_promo('10', self.promo_media,10), 7, [-1], 10, None)
        self.root[11] = USSDOption(self.promo_media_gb, self.activate_package_promo('10', self.promo_media_gb,11), 7, [-1], 10, None)
        self.root[12] = USSDOption('Menu *100#', None, None, [13,14], None, None)
        self.root[13] = USSDOption('Consultar Saldo', None, 12, [-1], None, self.get_actual_balance)
        self.root[14] = USSDOption('Consultar paquete  actual', None, 12, [-1], None, self.get_actual_package)
    
    def charge_balance(self, balance, id):
        self.balances.add(id)
        return 'Saldo recargado de %s USD.' % balance
    
    def activate_package(self, balance, id):
        self.packages.add(id)
        return 'Paquete activado de %s USD.' % balance
    
    def activate_package_promo(self, balance, detail, id):
        self.packages.add(id)
        return 'Paquete activado de %s USD, %s.' % (balance, detail)
    
    def set_package(self, id):
        if id not in self.packages or self.actual_balance < self.root[id].value:
            return False
        self.actual_package = self.root[id].name
        self.actual_balance -= self.root[id].value
        return True
        
    def set_balance(self, id):
        if id not in self.balances:
            return False
        self.actual_balance += self.root[id].value
        return True
    
    def set_activity(self, id):
        if id in self.balances:
            return self.set_balance(id)
        if id in self.packages:
            return self.set_package(id)
        return False
    
    def get_actual_package(self):
        package = 'Ninguno'
        if self.actual_package is not None:
            package = self.actual_package
        return 'Su paquete actual es %s.' % package
    
    def get_actual_balance(self):
        return 'Su saldo actual es %d USD.' %  self.actual_balance