from flask import Flask
from flask import  render_template, request

from circuts import eight_bit_full_adder

app = Flask(__name__)

nums = [[False for _ in range(8)], [False for _ in range(8)]]

@app.route("/")
def main_page():
    return render_template("main.html")

@app.route('/update_toggle', methods=['POST'])
def update_toggle():
    #num1/2 = [3] indx = [-1]
    id = request.form['id']
    status = request.form['status']
    nums[int(id[3])][(int(id[-1]))] = True if status == "true" else False
    return eight_bit_full_adder(0, nums[0], nums[1])
    
if __name__ == "__main__":
    app.run(debug=True, port=5001)
