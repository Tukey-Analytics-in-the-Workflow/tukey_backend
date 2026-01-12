import tableauserverclient as TSC

from fastapi import APIRouter, UploadFile
import pandas as pd

from ..utils.hyper_utils import convert_to_hyper_file
from ..config.config import TABLEAU_SERVER_URL, TABLEAU_PROJECT_ID, TABLEAU_PAT_NAME, TABLEAU_PAT_SECRET, TABLEAU_SITE_ID, TABLEAU_WORKBOOK_TEMPLATE

router = APIRouter()

@router.post("/upload")
async def upload_pos(file: UploadFile):
    df = pd.read_csv(file.file)

    file_name = file.filename.split(".")[0]
    hyper_file_location = f'./tmp/{file_name}.hyper'

    # convert to hyper file
    convert_to_hyper_file(df, hyper_file_location)

    tableau_auth = TSC.PersonalAccessTokenAuth(
        TABLEAU_PAT_NAME,
        TABLEAU_PAT_SECRET,
        site_id=TABLEAU_SITE_ID
    )

    tableau_server = TSC.Server(TABLEAU_SERVER_URL, use_server_version=True)

    with tableau_server.auth.sign_in(tableau_auth):

        # creating a new workbook
        # new_workbook = TSC.WorkbookItem('381e65eb-a76a-4519-bf11-ca69642b9c22')
        # publishing a data source
        print('Publishing a data source')

        new_datasource = TSC.DatasourceItem(TABLEAU_PROJECT_ID)

        updated_datasource = tableau_server.datasources.publish(
            new_datasource,
            hyper_file_location,
            TSC.Server.PublishMode.Overwrite,
            connection_credentials=None,
            as_job=False
        )

        print(f'Datasource {updated_datasource.name} published successfully')

        print(f'Updated Datasource ID: {updated_datasource.id}')

        # now creating a workbook
        print("Now creating a workbook")

        workbook_item = TSC.WorkbookItem(TABLEAU_PROJECT_ID, name=file_name)

        workbook_item = tableau_server.workbooks.publish(workbook_item, TABLEAU_WORKBOOK_TEMPLATE,
                                                         TSC.Server.PublishMode.Overwrite,
                                                         as_job=False)

        print("Workbook published")

        # once the workbook item is created, next thing is to publish it, this is done
        tableau_server.workbooks.populate_views(workbook_item)

        # now checking the view source
        for view in workbook_item.views:
            print("View Name:", view.name)
            print("View ID:", view.id)
            print("Content URL:", view.content_url)



        # MVP: just validate & preview
        return {
            "urls": [
                view.content_url.replace('sheets/', '') for view in workbook_item.views
            ]
        }
