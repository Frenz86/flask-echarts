from random import randrange

from flask import Flask, render_template

from pyecharts import options as opts
from pyecharts.charts import Bar
import pandas as pd

df = pd.DataFrame({'x':[1,2,3], 'y':[4,2,6]})

app = Flask(__name__, static_folder="templates")


def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(list(df.x))
        .add_yaxis("lamia_y", list(df.y))
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-Chart", subtitle="sottotitolo"))
    )
    return c


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()


if __name__ == "__main__":
    app.run()