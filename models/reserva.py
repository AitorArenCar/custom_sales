from odoo import models, fields, api

class Reserva(models.Model):
    _name = 'reservas.reserva'
    _description = 'Reserva'

    cliente_id = fields.Many2one('res.partner', string="Cliente")
    producto_id = fields.Many2one('reservas.producto', string="Producto")
    fecha_reserva = fields.Date(string="Fecha de Reserva")
    estado = fields.Selection([('pendiente', 'Pendiente'), ('enAlmacen', 'En almacén') ('recogida', 'Recogida')], string="Estado")
    descuento = fields.Float(string="Descuento")
    dias_reserva = fields.Integer(string="Dias de reserva", required=True)

