import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    self_viewed = views[
        views["author_id"] == views["viewer_id"]
    ]

    unique_author = (
        self_viewed["author_id"]
        .drop_duplicates()
        .sort_values()
    )

    return pd.DataFrame({"id": unique_author})
