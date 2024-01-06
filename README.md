## Run project
Clone:

``` git clone --recursive git@github.com:gustavorayo/video-to-cartoon.git ```

```cd  video-to-cartoon```

Install dependencies

```pip install -r requirements.txt```

```python install.py```

Usage:
```
python vid2cartoon.py --input_video <source_video> --style <style_to_apply> --frames <frames_to_translate> --output <output_video_name>
```
styles supported:
- Van-Gogh
- ghibli
- ryo

Example:
```
python vid2cartoon.py --input_video ./dataset/01.mp4 --style ghibli --frames 91 --output test.mp4
```
## Translation examples
| Video                                                                                                       | Ryo Takemas | Ghibli | Van Gogh |
|-------------------------------------------------------------------------------------------------------------| ----- | ---- | ---- |
| ![01](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/acbcd8a9-ebf3-4be1-8e33-766dc355e529)  |![01_ryo](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/8407e3b2-562c-4559-aabc-2f79d7b76c46) |![01_ghibli](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/301b0566-b869-459a-93bc-4ad74209dddf) | ![01_van_gogh](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/68ac0eac-c11a-4bcf-b6ee-cde22051f989) |
| ![02](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/cbdf009f-5c19-4c73-9930-ad445b53a92c)  |![02_ryo](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/b854bdb5-9c5b-47fe-9bea-24dc222fc558) |![02_ghibli](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/8199020e-24d4-4803-8e91-e29d104c35b9) | ![02_van_gogh](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/bfe5b053-3726-40c7-930d-7fa747b0c726) |
| ![03](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/2f0d0a72-2536-47bf-bcb2-537959ce71c6)  |![03_ryo](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/acdc9674-e5c0-474d-b0ca-79e8da811217) |![03_ghibli](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/93cd7863-67e2-4cf7-afb6-d0fcc1dcf570) | ![03_van_gogh](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/60e9e020-1c33-43de-b5ec-87c845b8b25a) |
| ![04](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/3aaaf2b4-655e-4f7b-95bf-7aaaeab985fe)  |![04_ryo](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/9b25e414-f1b7-4d3f-b716-a77befa1a4ca) |![04_ghibli](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/4bdd3248-c946-4569-bcd6-207fc087ee97) | ![04_van_gogh](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/71d42a53-37e1-4258-b2d4-0979faf0beb4) |
| ![05](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/233cd37f-e4a1-4a14-93ed-517c526ca5b4)  |![05_ryo](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/adeb9742-606d-4db2-8a78-a72334fd17f6) |![05_ghibli](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/7daf82bc-346e-4b1c-916b-7d0b211e79e4) | ![05_van_gogh](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/8c51c453-f7c5-497d-be77-32e4b049322a) |
| ![06](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/9f5b11b6-9d41-408c-818c-e64e0156fa3d)  |![06_ryo](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/23ddc9f8-7bcd-4d8d-8136-73006b5e4dec) |![06_ghibli](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/fb60e4d0-0637-4f53-b7e3-f7c7272964da) | ![06_van_gogh](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/f46d3bdd-2357-4c81-9b7b-deefce8449e9) |
| ![07](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/d1f46b52-e3fd-48f4-9005-bcd45e083fcb)  |![07_ryo](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/bc5e0c47-d81b-4268-a2a3-c94ea20c4307) |![07_ghibli](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/16bdc1f5-dd2e-486e-8ca7-b5cb14e32338) | ![07_van_gogh](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/b67c70e0-ac02-4903-b1cb-f70224017dcb) |
| ![08](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/5794424a-32bc-4c2b-a122-57697c7723e6)  |![08_ryo](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/7e157ee9-9951-4458-9048-7ce8700b4cef) |![08_ghibli](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/985a4916-eda3-4933-8261-5ad4331350a3) | ![08_van_gogh](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/06e53c02-fad9-4afb-8376-53e1a5b3fb08) |
| ![09](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/14cb04f6-916c-4545-9af5-c62c788029fd)  |![09_ryo](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/fd92a58d-335f-442b-9080-4a3d69e46483) |![09_ghibli](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/d56001c7-e438-41e6-8751-019211be1be7) | ![09_van_gogh](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/c96d0577-4619-4d3c-8f03-19b39fd76dca) |
| ![10](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/f3dbc759-2579-4b5d-b2ec-4173029c4c21)  |![10_ryo](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/fbfbb0bc-a49a-4081-96e8-74b56d358556) |![10_ghibli](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/0acfbc4a-1be5-4adb-9a72-f069e966fc09) | ![10_van_gogh](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/8ae047cc-3542-419e-b3a1-a8d210e046c9) |
| ![11](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/ef0fe96c-094d-4e24-a118-3a7cba58cfd5)  |![11_ryo](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/533cfdf0-14ab-49cb-b227-f5c963354cd1) |![11_ghibli](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/d2e4a9d5-56f1-4b9e-b45c-b173766b0d1d) | ![11_van_gogh](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/8cd7ffa7-e443-4d0c-a4fd-e2fee7562424) |
| ![12](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/11cdf0ec-6a99-4b25-9e29-e25943b5917d)  |![12_ryo](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/2337c665-fe20-48c7-ac94-9e798b26103f) |![12_ghibli](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/bee32426-dd40-47df-a5c9-a0d736388618) | ![12_van_gogh](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/1bfe2a9a-545a-4d56-9c01-ceabffeb599d) |
| ![13](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/8cc4e2d4-9590-4a44-ac62-099e06eaf6ff)  |![13_ryo](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/225afb26-5197-4751-86c0-90ac0397ab46) |![13_ghibli](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/788a6eae-230e-4f7e-bf5f-68831d2046f3) | ![13_van_gogh](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/57b36021-4a1d-4467-a9a2-ec297c2e3622) |
| ![14](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/197c8ceb-1eb5-4964-8c4c-5dc93f3747d5)  |![14_ryo](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/fd450115-d354-4e80-b807-a08fb9d22a11) |![14_ghibli](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/3e63e5ed-5bb2-45fc-82b0-235939fdad68) | ![14_van_gogh](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/06340853-efb8-4d6b-9b30-da916f484ea0) |
| ![15](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/a585129b-ef41-440c-9283-e6a0153235a4)  |![15_ryo](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/935a2586-7f2d-4944-ab56-2a02507429a3) |![15_ghibli](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/09886651-2911-487a-8955-6e6bf0c6949c) | ![15_van_gogh](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/5cce1188-7ce1-4e84-be3e-7f1c6852d111) |
| ![16](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/8dc21330-acb1-465a-bac9-75ec0ae50d06)  |![16_ryo](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/3d878c33-1297-4c87-974e-ce1d611369d4) |![16_ghibli](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/34135a97-6f6d-4b9a-86f2-ff0db0a701df) | ![16_van_gogh](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/3b5abe95-b27d-461b-9627-9ec27af46e29) |
| ![17](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/111c0928-5586-4d45-befa-359296ca8e92)  |![17_ryo](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/ef25f994-d5b7-47a4-b6fe-6d9954c2d808) |![17_ghibli](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/a5a5ea8f-3740-4a88-bcb3-270c3cce5b4a) | ![17_van_gogh](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/4b0483ef-c602-4a26-9212-c3e9a62cd33c) |
| ![18](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/927770f9-b9e3-40e7-ae49-1406f33754e0)  |![18_ryo](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/5b6939d1-8b12-4dbf-9aca-6b67cfa84224) |![18_ghibli](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/2b6b9edb-6dd5-4da1-96e7-508f9792540d) | ![18_van_gogh](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/74dc354f-45a6-42b6-9b92-63af27fd98e6) |
| ![19](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/c0ab09c8-1fb1-46ff-abb8-5e1e6a65caf0)  |![19_ryo](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/5cefc0ff-29ae-4d59-9a24-a0b64aecbe64) |![19_ghibli](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/5954b361-4cd6-43be-91b2-34f3797b4440) | ![19_van_gogh](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/a2f1ab5d-9013-4f16-9859-b7f9a14ba8ee) |
| ![20](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/10c86e24-eebd-4630-9e38-ca8566ad9936)  |![20_ryo](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/0509e6f5-de6d-4c6e-bb70-09b1b9f30775) |![20_ghibli](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/86d89f2c-018e-4ec0-b82d-78d18e74fa11) | ![20_van_gogh](https://github.com/gustavorayo/video-to-cartoon/assets/1848141/1870f2fd-373d-41d5-9b19-ccf135d8c2fb) |


