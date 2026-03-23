import marimo

__generated_with = "0.21.1"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## What's up here ?
    In this part we are going to track the population dynamics of our two entities :
    - the wildfires
    - the forest (the trees)

    In order to do this we proceed regardless of space dimension, we only conservate the time dimension.

    To do so, we integrated the system over the two spaces dimensions.

    Finally, we get this dynamic system :
    """)
    return


if __name__ == "__main__":
    app.run()
