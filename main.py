from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Deasal Tour and Travel</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f4f8fb;
        }
        header {
            background: linear-gradient(to right, #0077b6, #00b4d8);
            color: white;
            padding: 25px;
            text-align: center;
        }
        nav {
            background: #023e8a;
            padding: 12px;
            text-align: center;
        }
        nav a {
            color: white;
            margin: 15px;
            text-decoration: none;
            font-weight: bold;
        }
        section {
            padding: 40px;
        }
        .hero {
            background: url('https://images.unsplash.com/photo-1500530855697-b586d89ba3ee') center/cover;
            color: white;
            text-align: center;
            padding: 100px 20px;
        }
        .hero h1 {
            font-size: 45px;
        }
        .cards {
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
        }
        .card {
            background: white;
            width: 300px;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 3px 8px gray;
        }
        .card h3 {
            color: #0077b6;
        }
        form {
            background: white;
            padding: 25px;
            max-width: 450px;
            border-radius: 10px;
            box-shadow: 0 3px 8px gray;
        }
        input, textarea, button {
            width: 100%;
            padding: 12px;
            margin-top: 10px;
        }
        button {
            background: #0077b6;
            color: white;
            border: none;
            font-size: 16px;
            cursor: pointer;
        }
        footer {
            background: #023e8a;
            color: white;
            text-align: center;
            padding: 15px;
        }
    </style>
</head>
<body>

<header>
    <h1>Deasal Tour and Travel</h1>
    <p>Your trusted partner for memorable journeys</p>
</header>

<nav>
    <a href="#home">Home</a>
    <a href="#packages">Packages</a>
    <a href="#about">About</a>
    <a href="#contact">Contact</a>
</nav>

<div class="hero" id="home">
    <h1>Explore Beautiful Destinations</h1>
    <p>Best travel packages for Ladakh, Kashmir, and more</p>
</div>

<section id="packages">
    <h2>Our Tour Packages</h2>
    <div class="cards">
        <div class="card">
            <h3>Ladakh Tour</h3>
            <p>Explore Leh, Nubra Valley, Zanskar Valley, Pangong Lake and monasteries.</p>
            <b>Starting from ₹15,999</b>
        </div>

        <div class="card">
            <h3>Kashmir Tour</h3>
            <p>Visit Srinagar, Gulmarg, Pahalgam and Dal Lake.</p>
            <b>Starting from ₹12,999</b>
        </div>

        <div class="card">
            <h3>Himachal Tour</h3>
            <p>Enjoy Manali, Shimla, Kasol and mountain adventures.</p>
            <b>Starting from ₹10,999</b>
        </div>
    </div>
</section>

<section id="about">
    <h2>About Us</h2>
    <p>
        Deasal Tour and Travel provides safe, affordable and comfortable travel
        services. We offer customized tour packages, hotel booking, taxi services
        and adventure trips for families, students and groups.
    </p>
</section>

<section id="contact">
    <h2>Contact Us</h2>

    {% if message %}
        <h3 style="color:green;">{{ message }}</h3>
    {% endif %}

    <form method="POST">
        <input type="text" name="name" placeholder="Enter your name" required>
        <input type="email" name="email" placeholder="Enter your email" required>
        <input type="text" name="phone" placeholder="Enter your phone number" required>
        <textarea name="message" placeholder="Write your message" rows="5" required></textarea>
        <button type="submit">Send Enquiry</button>
    </form>
</section>

<footer>
    <p>&copy; 2026 Deasal Tour and Travel | All Rights Reserved</p>
</footer>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        name = request.form["name"]
        message = f"Thank you {name}, your enquiry has been received!"
    return render_template_string(HTML, message=message)

if __name__ == "__main__":
    app.run(debug=True)


    @app.route('/deasal')
    def home():
        return "Welcome to Deasal Tour and Travel"