from flask import Blueprint
from ..models.cat import cats
#doble punto te devuelve al directorio de app

cats_bp = Blueprint("cats_bp", __name__, url_prefix="/cats")


#Get informastion for a single cat 
@cats_bp.get("")
def get_all_cats():
    results_list = []
    
    for cat in cats:
        results_list.append(dict(
            id = cat.id,
            name = cat.name,
            color = cat.color,
            personality = cat.personality
        ))
        
    return results_list


@cats_bp.get("/<cat_id>")
def get_cat_by_id(cat_id):
    try:
        cat_id = int(cat_id)
    except ValueError:
        return {"message": f"Cat {cat_id} invalid"}, 400
    
    
    for cat in cats:
        if cat.id == cat_id:
            return dict(
                id = cat.id,
                name = cat.name,
                color = cat.color,
                personality = cat.personality
                
            )
#If cat Id does NOT exist            
    return {"message": f"Cat {cat_id} not found"}, 404
            
    