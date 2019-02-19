import psycopg2

DB_NAME = "news"


def get_top3_articles():
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute("select articles.title, count(slug) from articles, log where"
              " path like '%' || slug group by title order by"
              "count(slug) desc limit 3;")
    return c.fetchall()


def get_top_authors():
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute("select name, views from authors join (select articles.author,"
              "count(slug) as views from articles, log where path like '%'"
              "|| slug group by articles.author order by count(slug) desc) "
              "as subq on id = subq.author;")
    return c.fetchall()


def get_err_log():
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute("select wtime, (cast(error_view.cnt as decimal) "
              "* 100 / whole_view.cnt) as err from whole_view, "
              "error_view where wtime = etime and"
              "(cast(error_view.cnt as decimal)"
              "* 100 / whole_view.cnt) > 1;")
    return c.fetchall()


if __name__ == "__main__":
    print("Welcome to the reportingM!\n")
    print("please enter a number by following instruction below")
    print("1. The most popular three articles of all time")
    print("2. The most popular article authors of all time")
    print("3. The days more than 1% of requests led to errors\n")
    number = input("Please type a number: ")
    if number == 1:
        info = get_top3_articles()
        for i in range(len(info)):
            print("{au} -- {vi} views".format(au=info[i][0], vi=info[i][1]))
    if number == 2:
        info = get_top_authors()
        for i in range(len(info)):
            print("{au} -- {vi} views".format(au=info[i][0], vi=info[i][1]))
    if number == 3:
        info = get_err_log()
        for i in range(len(info)):
            print("{au} -- {vi}% errors".format(au=info[i][0], vi="{0:.2}"
                                                .format(info[i][1])))
