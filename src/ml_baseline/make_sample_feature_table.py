import pandas as pd
import numpy as np
import pathlib as Path

def make_sample_feature_table(*, root: Path | None =None, n_users: int =50, seed: int =42)-> Path:
    """Create a simple sample feature table."""

    data = {
        'order_id': range(1, n_users + 1),
        'customer_age': np.random.randint(18, 70, n_users),
        'total_spent': np.random.uniform(10, 500, n_users).round(2),
        'num_orders': np.random.randint(1, 20, n_users),
        'country': np.random.choice(['SA', 'UK', 'DE', 'FR', 'US'], n_users),
        'avg_amount': np.random.uniform(10, 100, n_users).round(2),
        'total_amount': np.random.uniform(50, 1000, n_users).round(2),
    }

    df = pd.DataFrame(data)

    df['is_high_value'] = (df['total_amount'] > 300).astype(int)
    if root is not None:
        path = root / "orders_clean.parquet"
        path.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(path, index=False)
    else:
        path = None
    return path