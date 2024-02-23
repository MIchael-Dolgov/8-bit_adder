from flask import Flask
from flask import  render_template, request

from circuts import eight_bit_full_adder, eight_bit_full_substractor

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
    isminus = True if request.form['sign'] == "true" else False
    if (len(id)!=1):
        nums[int(id[3])][(int(id[-1]))] = True if status == "true" else False
    if (isminus):
        print("substractor")
        return eight_bit_full_substractor(nums[0], nums[1])
    else: 
        print("adder")
        return eight_bit_full_adder(0, nums[0], nums[1])

if __name__ == "__main__":
    app.run(debug=True)
