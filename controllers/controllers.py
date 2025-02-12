from odoo import http
from odoo.http import request
from odoo.exceptions import UserError

class ReservaController(http.Controller):
    
    @http.route('/reservas/web/form', type='http', auth="public", website=True)
    def reserva_form(self, **kwargs):
        """
        Página de formulario para hacer una reserva
        """
        # Recuperar todos los productos disponibles
        productos = request.env['reservas.producto'].search([])
        return request.render('reservas_custom.reserva_form', {
            'productos': productos
        })
    
    @http.route('/reservas/web/submit', type='http', auth="public", website=True, methods=['POST'])
    def reserva_submit(self, **kwargs):
        """
        Lógica para procesar la reserva del cliente
        """
        cliente_id = request.env.user.partner_id.id  # Usuario logueado como cliente
        producto_id = kwargs.get('producto_id')
        fecha_reserva = kwargs.get('fecha_reserva')
        descuento = kwargs.get('descuento')
        
        # Validar los datos
        if not (producto_id and fecha_reserva and descuento):
            raise UserError("Todos los campos son obligatorios")

        # Crear la reserva
        reserva = request.env['reservas.reserva'].create({
            'cliente_id': cliente_id,
            'producto_id': int(producto_id),
            'fecha_reserva': fecha_reserva,
            'descuento': float(descuento),
            'estado': 'pendiente',
            'dias_reserva': 30
        })
        
        return request.render('reservas_custom.reserva_confirmation', {
            'reserva': reserva
        })
