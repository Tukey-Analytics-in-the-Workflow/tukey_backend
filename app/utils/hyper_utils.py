from tableauhyperapi import SqlType, TableDefinition, HyperProcess, Telemetry, Connection, CreateMode, Inserter

import pandas as pd


def pandas_to_hyper_schema(df: pd.DataFrame):
    columns = []

    for col, dtype in df.dtypes.items():

        if pd.api.types.is_integer_dtype(dtype):
            sql_type = SqlType.big_int()
        elif pd.api.types.is_float_dtype(dtype):
            sql_type = SqlType.double()
        elif pd.api.types.is_bool_dtype(dtype):
            sql_type = SqlType.bool()
        elif pd.api.types.is_datetime64_any_dtype(dtype):
            sql_type = SqlType.timestamp()
        else:
            sql_type = SqlType.text()

        columns.append(TableDefinition.Column(str(col), sql_type))

    return columns


def convert_to_hyper_file(df: pd.DataFrame, output_path: str):
    columns = pandas_to_hyper_schema(df)

    with HyperProcess(Telemetry.DO_NOT_SEND_USAGE_DATA_TO_TABLEAU) as hyper_process:
        with Connection(
                endpoint=hyper_process.endpoint,
                database=output_path,
                create_mode=CreateMode.CREATE_AND_REPLACE
        ) as conn:
            table = TableDefinition(
                table_name='Extract.Extract',
                columns=columns
            )

            conn.catalog.create_table(table)

            with Inserter(conn, table) as inserter:
                inserter.add_rows(df.itertuples(index=False))
                inserter.execute()
