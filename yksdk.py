from yookassa import Refund
from yookassa import Configuration
from yookassa import Receipt
from config import ykid, secret
import uuid

Configuration.account_id = ykid
Configuration.secret_key = secret

refund = Refund.create({
    "amount": {
        "value": "2000.00",
        "currency": "RUB"
    },
    "payment_id": "2c0979a2-000f-5000-a000-1e68a26b968e"
})
#
# idempotence_key = str(uuid.uuid4())
#
# response = Receipt.create({
#     "customer": {
#         "full_name": "Ivanov Ivan Ivanovich",
#         "email": "email@email.ru",
#         "phone": "+79211234567",
#         "inn": "6321341814"
#     },
#     "payment_id": "2c092f88-000f-5000-a000-115c467b89ca",
#     "type": "payment",
#     "send": True,
#     "items": [
#         {
#             "amount": {
#                 "value": "1700.00",
#                 "currency": "RUB"
#             },
#             "quantity": "1.00",
#             "description": "Оплата записи 2'nd line filial",
#             "recipient": {
#                 "account_id": "209949",
#                 "gateway_id": "2058913"
#             },
#             "vat_code": "1",
#             "payment_mode": "full_payment",
#             "payment_subject": "service"
#         }
#     ],
#     "settlements": [
#         {
#             "type": "prepayment",
#             "amount": {
#                 "value": "1700.00",
#                 "currency": "RUB"
#             },
#         }
#     ]
# }, idempotence_key)
