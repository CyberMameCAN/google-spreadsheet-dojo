import os

from dotenv import load_dotenv

import gspread


class SpreadSheets:
    """
    グーグルスプレッドシート基本クラス
    
    スプレッドシートのオブジェクトを作成する
    """
    def __init__(self, sheet_key, credentials):
        self.sheet_key = sheet_key
        self.credentials = credentials

    def get_credentials(self):
        return gspread.service_account(self.credentials)

    def get_sheet(self):
        gc = self.get_credentials()
        return gc.open_by_key(self.sheet_key)

    def get_worksheet_list(self) -> list:
        """シートの一覧を一次元配列に格納する"""
        sh = self.get_sheet()
        worksheet_list = sh.worksheets()
        return worksheet_list

    def create_worksheet(self, title: str) -> bool:
        """ワークシートを追加する
        既にある時はエラーになる
        """
        sh = self.get_sheet()
        try:
            sh.add_worksheet(title=title, rows=100, cols=26)
            return True

        except Exception as e:
            print(e)
            return False

    def deleat_worksheet(self, title: str) -> bool:
        """ワークシートを削除する"""
        sh = self.get_sheet()
        try:
            worksheet = sh.worksheet(title)
            sh.del_worksheet(worksheet)
            return True

        except Exception as e:
            print(e)
            return False


class WorkSheet:
    """ワークシートを操作するクラス"""
    def __init__(self, ss: SpreadSheets, worksheet_name):
        self.worksheet_name = worksheet_name

        _sh = ss.get_sheet()
        self.worksheet = _sh.worksheet(self.worksheet_name)

    def write(self, vals: list):
        """ １行追加 """
        self.worksheet.append_row(vals)
        print(f"シートに書き込みました。")

    def write_many(self, vals: list):
        """ 複数行追加 """
        self.worksheet.append_rows(vals)
        print(f"シートに書き込みました。")

    def read(self):
        """セルのデータを読み込む"""
        #return worksheet.range('A1:D3')
        cell_list = self.worksheet.get_all_values()
        return cell_list

    def read_range(self, r: str):
        """
        セルのデータを読み込む
            r: EX) 'A1:B3', 'C6'
        """
        return self.worksheet.range(r)

    def get_meta(self) -> str:
        """シートのタイトルを返す"""
        #worksheet = self.get_worksheet()
        return self.worksheet.title


class FuncFactory:
    def __init__(self):
        load_dotenv()
        self.SHEET_KEY = os.environ['SHEET_KEY']
        self.CREDENTIALS = os.environ['CREDENTIALS']
        self.WORKSHEET_NAME = os.environ['WORKSHEET_NAME']

    def selector(self, func_type: str):
        ss = SpreadSheets(self.SHEET_KEY, self.CREDENTIALS)

        if func_type == 'worksheet_list':
            print(ss.get_worksheet_list())

        elif func_type == 'write':
            ws = WorkSheet(ss, self.WORKSHEET_NAME)
            ws.write(['G', '7', 'x', '18'])
        
        elif func_type == 'write_many':
            ws = WorkSheet(ss, self.WORKSHEET_NAME)
            ws.write_many([['f', '8', 'X', '88'],
                           ['F', '8', 'Y', '80']])
        
        elif func_type == 'read':
            ws = WorkSheet(ss, self.WORKSHEET_NAME)
            print(ws.read())
        
        elif func_type == 'read_range':
            ws = WorkSheet(ss, self.WORKSHEET_NAME)
            print(ws.read_range('C11:D11'))
        
        elif func_type == 'get_meta':
            ws = WorkSheet(ss, self.WORKSHEET_NAME)
            print(ws.get_meta())
        
        elif func_type == 'make_worksheet':
            junk_sheet_name = 'from_python'
            is_maked = ss.create_worksheet(junk_sheet_name)
            if is_maked:
                print('[OK] シート作成')
            else:
                print('[ERRORE] シート作成失敗')
        
        elif func_type == 'deleat_worksheet':
            junk_sheet_name = 'from_python'
            is_deleated = ss.deleat_worksheet(junk_sheet_name)
            if is_deleated:
                print('[OK] シート削除')
            else:
                print('[ERRORE] シート削除失敗')
        else:
            raise AttributeError(f"ValueError func_type ? '{func_type}'")


def main():
    try:
        f2 = FuncFactory()
        f2.selector('write')

    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"[ERROR] {e}")


if __name__ == '__main__':
    main()
