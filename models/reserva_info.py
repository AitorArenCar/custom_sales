from odoo import models, fields, api

# no tiene mucho sentido este modelo por ahora, lo comento
class ReservaInfo(models.Model):
    _name = 'reservas.info'
    _description = 'Información sobre cada reserva según producto'

    producto_id = fields.Many2one('reservas.producto', string="Producto")
    llegada_aprox = fields.Date(string="Llegada aproximada")
    dias_reserva = fields.Integer(string="Dias de reserva", required=True)
    cantidad = fields.Integer(string="Cantidad de reservas del producto", required=True) # lo he movio a reserva