#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flet as ft
import os
import test

def main(page: ft.Page):

   


        
    
    error_flag = -1
    selected_filepath = ft.Text()
    
    def file_pick_fn(e: ft.FilePickerResultEvent):
        selected_file.value = ", ".join(map(lambda f:f.name, e.files)) if e.files else "Cancelled"
        selected_file.update()
        selected_filepath.value = ", ".join(map(lambda f:f.path, e.files)) if e.files else "Cancelled"  
        selected_filepath.update()      
       # print(selected_filepath)
    pick_file_dialog = ft.FilePicker(on_result=file_pick_fn) # on_result：結果投げる宛先を指定
    selected_file = ft.TextField(border="underline",read_only=True)

    page.overlay.append(pick_file_dialog)

    def check_btn(e):
        if not selected_filepath.value:
            selected_filepath.error_value = "ファイルを選択してください"
            page.update()
        else:
            path = selected_filepath.value
            read = test.file_open(path)
            
            
    

    data = ft.DataTable(
            width=700,
            bgcolor="white",
            #border=ft.border.all(2, "gray"),
            #border_radius=10,
            #vertical_lines=ft.border.BorderSide(3, "black"),
            horizontal_lines=ft.border.BorderSide(1, "gray"),
            sort_column_index=0,
            sort_ascending=True,
            heading_row_color=ft.colors.BLACK12,
            heading_row_height=100,
            data_row_color={"hovered": "0x30FF0000"},
            show_checkbox_column=True,
            divider_thickness=0,
            column_spacing=300,
            columns=[
                ft.DataColumn(
                    ft.Text("Time"),
                    tooltip="アクセス時刻",
                    on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
                ),
                ft.DataColumn(
                    ft.Text("URL"),
                    tooltip="アクセスされたドメイン",
                    numeric=True,
                    on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
                ),
            ],
            rows=[
                ft.DataRow(
                    [ft.DataCell(ft.Text()), ft.DataCell(ft.Text("1"))],
                    selected=True,
                    on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                ),
                ft.DataRow(
                    [ft.DataCell(ft.Text("B")), ft.DataCell(ft.Text("2"))],
                    selected=False

                ),
            ],
        )
    
    tab = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="URL List",
                content=ft.Container(
                    content=data
                ),
                
            ),
            ft.Tab(
                text="Bad TLD List",
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                text="Reputation Checker",
                content=ft.Text("This is Tab 3"),
            ),
        ],
        expand=1,
    )
     
     
    
    
    page.add(
        ft.Row(
            [
            ft.ElevatedButton("選択されたファイル",
                              on_click = lambda _: pick_file_dialog.pick_files(
                                  allow_multiple = True
                              )),
            selected_file,
            #selected_filepath,
            ]
        ),
        
        ft.Row(
            [
            ft.FilledButton(text="Check", on_click=check_btn),
           # selected_filepath,    
           # ft.FilledButton(text="URL List"),
           # ft.FilledButton(text="Bad TLD Check"),
           # ft.FilledButton(text="Reputation Check"),
           # ft.FilledButton(text="Export to .xlsx"),
            ]
        ),
        tab

       

    )


          

ft.app(target=main)
