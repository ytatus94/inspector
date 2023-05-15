def get_sub_dataframe(
        df,
        wid=None,
        pid=None,
        pids=None,
        pairs=None,
        start_date=None,
        end_date=None,
        cols=None,
        verbose=False
    ):
    if verbose:
        print(f'Call get_sub_dataframe(): wid={wid}, pid={pid}, pairs={pairs}, start_date={start_date}, end_date={end_date}')

    df_sub = df
    if wid is not None:
        df_sub = df_sub.loc[df_sub['warehouse_id']==wid]
    if pid is not None:
        df_sub = df_sub.loc[df_sub['product_id']==pid]
    if pids is not None:
        df_sub = df_sub.loc[df_sub['product_id'].isin(pids)]
    if pairs is not None:
        all_pids = [int(pairs.split(',')[1].replace(')', '')) for pair in pairs]
        df_sub = df_sub.loc[df_sub['product_id'].isin(all_pids)]
    if start_date is not None:
        df_sub = df_sub.loc[df_sub['date']>=start_date]
    if end_date is not None:
        df_sub = df_sub.loc[df_sub['date']<=end_date]
    if cols is not None:
        df_sub = df_sub.loc[:, cols]

    return df_sub

