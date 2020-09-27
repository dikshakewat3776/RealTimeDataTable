# from django.test import TestCase
#
# # Create your tests here.
# from flask import Flask, render_template
# import matplotlib.pyplot as plt
#
# app = Flask(__name__)
#
#
# @app.route('/plot')
# def plot():
#     left = [1, 2, 3, 4, 5]
#     height = [10, 24, 36, 40, 5]
#     tick_label = ['one', 'two', 'three', 'four', 'five']
#     plt.bar(left, height, tick_label=tick_label, width=0.8, color=['red', 'green'])
#
#     plt.ylabel('y - axis')
#     plt.xlabel('x - axis')
#     plt.title('My bar chart!')
#
#     plt.savefig('static/img/plot.png')
#
#     return render_template('plot.html', url='/static/img/plot.jpg')
#
#
# if __name__ == '__main__':
#    app.run()