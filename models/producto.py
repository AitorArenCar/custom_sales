from odoo import models, fields, api

class Producto(models.Model):
    _name = 'reservas.producto'
    _description = 'Producto disponible para reservas'

    nombre = fields.Char(string="Nombre", required=True)
    precio = fields.Float(string="Precio", required=True)
    descripcion = fields.Text(string="Descripción")
    reserva_ids = fields.One2many("reservas.reserva", "producto_id")
    cantidad_reservas = fields.Integer(string="Cantidad de reservas del producto", compute="_compute_cantidad_reservas")
    llegada_aprox = fields.Date(string="Llegada aproximada")

    @api.depends("reserva_ids")
    def _compute_cantidad_reservas(self):
        for record in self:
            record.cantidad_reservas = len(record.reserva_ids)