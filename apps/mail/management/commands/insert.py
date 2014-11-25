import xlrd
import csv
from django.conf import settings

from django.core.management.base import BaseCommand
from optparse import make_option
from apps.mail.models.List import List
from apps.mail.models.Category import Category
from apps.mail.models.ListDetail import ListDetail


class Command(BaseCommand):
    data_delete = False

    option_list = BaseCommand.option_list + (
        make_option('--delete',
                    action='store_true',
                    dest='delete',
                    default=False,
                    help='Delete data'),
    )

    def handle(self, *args, **options):
        entity = args[0]

        if entity == 'all':

            self.insert_csv()
            #self.insert_mails()

    def insert_csv(self):
        # List.objects.all().delete()
        # Category.objects.all().delete()
        def get_quality(quality):
            if quality == 'A+':
                return ListDetail.QUALITY_EXCELLENT
            return ListDetail.QUALITY_REGULAR
        try:
            list_bago = List.objects.filter(name='Bago').first()
            list_bago.status=List.STATUS_INACTIVE
            list_bago.save()
        except:
            pass

        _list = List()
        _list.name = 'Bago'
        _list.sender = 'Bago'
        _list.email = 'comunicaciones@bagoperu.com.pe'
        _list.save()

        ROOT_PATH = settings.ROOT_PATH
        file_path = ROOT_PATH + '/apps/mail/management/dbdata/ultimo.csv'
        dataReader = csv.reader(open(file_path), delimiter=',', quotechar='"')

        for row in dataReader:
            quality = row[1]
            quality = get_quality(quality)

            category_name = row[2]
            categories = Category.objects.filter(
                name=category_name,
                list=_list
            )
            if categories.exists():
                category = categories.first()
            else:
                category = Category()
                category.name = category_name
                category.list = _list
                category.save()

            list_detail = ListDetail()
            list_detail.list = _list
            list_detail.email = row[0]
            list_detail.quality = quality
            list_detail.name = row[0].split('@')[0]
            list_detail.category = category
            list_detail.save()
            print(row[0])

    def insert_mails(self):
        List.objects.all().delete()
        ROOT_PATH = settings.ROOT_PATH
        file_path = ROOT_PATH + '/apps/mail/management/dbdata/mail.xlsx'
        workbook = xlrd.open_workbook(file_path)
        for sheet in workbook.sheet_names():
            _list = List()
            _list.name = sheet
            _list.save()

            worksheet = workbook.sheet_by_name(sheet)
            num_rows = worksheet.nrows - 1
            num_cells = worksheet.ncols - 1
            curr_row = 0
            while curr_row < num_rows:
                curr_row += 1
                row = worksheet.row(curr_row)
                print 'Row:', curr_row
                curr_cell = -1
                while curr_cell < num_cells:
                    #1 Nombre
                    #2 Correo
                    #3 Categoria
                    #4 Lista

                    curr_cell += 1
                    cell_value = worksheet.cell_value(curr_row, curr_cell)
                    if curr_cell == 0:
                        name = cell_value
                    if curr_cell == 1:
                        email = cell_value
                    if curr_cell == 2:
                        category_name = cell_value

                try:
                    category = Category.objects.get(name=category_name, list=_list)
                except:
                    category = Category()
                    category.name = category_name
                    category.list = _list
                    category.save()

                list_detail = ListDetail()
                list_detail.list = _list
                list_detail.email = email
                list_detail.name = name
                list_detail.category = category
                list_detail.save()
