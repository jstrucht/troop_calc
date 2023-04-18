from flask import Flask, request, render_template
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    @app.route("/", methods =["GET", "POST"])
    def home():
        troop_mix = None
        default_ratio = False
        if request.method == "POST":
    
            max_tier = int(request.form.get("max_tier"))
            max_march = int(request.form.get("max_march"))
            default_ratio = False
            try:
                high_tier_ratio = int(request.form.get("ratio_high"))
                mid_tier_ratio = int(request.form.get("ratio_mid"))
                low_tier_ratio = int(request.form.get("ratio_low"))
            except:
                high_tier_ratio = 3
                mid_tier_ratio = 5
                low_tier_ratio =2
                default_ratio = True

            if high_tier_ratio + mid_tier_ratio + low_tier_ratio != 10:
                default_ratio = True

            other_count = (1000 * (4*max_tier)) - 3000

            max_march = max_march - other_count

            high_tier = int(high_tier_ratio * (max_march/10))
            mid_tier = int(mid_tier_ratio * (max_march/10))
            low_tier = int(low_tier_ratio * (max_march/10))

            troop_mix = [high_tier,
                    max_tier,
                    mid_tier,
                    max_tier - 1,
                    low_tier,
                    max_tier - 2
            ]
                    
        return render_template("home.html", troop_mix=troop_mix, default_ratio=default_ratio)
    
    return app
