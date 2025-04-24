from flask import abort, Blueprint, make_response
# from ..models.cat import cats

cats_bp = Blueprint("cats_bp", __name__, url_prefix="/cats")

# Función auxiliar para validar gato
# def validate_cat(cat_id):
#     try:
#         cat_id = int(cat_id)
#     except ValueError:
#         invalid_error = {"message": f"Cat {cat_id} invalid"}
#         abort(make_response(invalid_error, 400))
    
#     for cat in cats:
#         if cat.id == cat_id:
#             return cat
    
#     not_found = {"message": f"Cat {cat_id} not found"}
#     abort(make_response(not_found, 404))

# # Obtener todos los gatos
# @cats_bp.get("/")
# def get_all_cats():
#     results_list = []

#     for cat in cats:
#         results_list.append({
#             "id": cat.id,
#             "name": cat.name,
#             "color": cat.color,
#             "personality": cat.personality
#         })

#     return results_list

# # Obtener gato por ID
# @cats_bp.get("/<cat_id>")
# def get_cat_by_id(cat_id):
#     cat = validate_cat(cat_id)
    
#     return {
#         "id": cat.id,
#         "name": cat.name,
#         "color": cat.color,
#         "personality": cat.personality
#     }
        