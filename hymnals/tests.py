from django.test import TestCase

# Create your tests here.

    # <form role="form" method="POST">
    # {% csrf_token %}
    #     <div class="btn-group" data-toggle="buttons">
    #         <label class="btn btn-primary">
    #             <input type="checkbox">Смешанный
    #         </label>
    #         <label class="btn btn-primary">
    #             <input type="checkbox">Мужской
    #         </label>
    #         <label class="btn btn-primary">
    #             <input type="checkbox">Молодежный
    #         </label>
    #     </div>
    #     <div>
    #         <input type="submit" class="btn btn-default" value="Запрос"/>
    #     </div>
    # </form>

    # <!--    <TR>
#         {% if date_list %}
#             <h2>{{ song_count }}</h2>
#             {% for song_vs_ws in date_list %}
#                 <tr>
#                     <TD>{{ song_vs_ws.Date}}</TD><TD></TD>
#                 </tr>
#             {% endfor %}
#         {% endif %}
#     </TR>-->

# <form role="form" method="POST">
#     {% csrf_token %}
#     <div class="form-group">
#         <input name="Name" type="text" class="form-control" placeholder="Название гимна"/>
#     </div>
#     <div class="form-group">
#         <input name="Authors" type="text" class="form-control" placeholder="Автор"/>
#     </div>
#     <div class="form-group">
#         <input type="submit" class="btn btn-default" value="Найти" />
#     </div>
# </form>


# <li class="active"><a href="{% 'hymnals:findform' '1' %}">Название</a></li>
#   <li><a href="{% 'hymnals:findform' '2' %}">Автор</a></li>

# <ul class="nav nav-tabs">
#   <li class="active"><a href="/hymnals/search/">По названию</a></li>
#   <li class="disabled"><a href="#">По автору</a></li>
# </ul>

            # {% for sing in song_table %}
            #     {% if sing.id = song. %}
            #         <td>1</td>
            #     {% else %}
            #         <td>0</td>
            #     {% endif %}
            # {% endfor %}

    # <table id="statisticTable">
    #     <tr>
    #         <td></td>
    #         {% for ws in ws_row %}
    #             <td width="20px" id="verticalRow">{{ ws.Date|date:"d E" }}</td>
    #         {% endfor %}
    #     </tr>
    # </table>



                # {% for sws in songrow %}
                #     {% if sws.time == ws.time %}
                #             <td width="20px" bgcolor="{{tdcolor}}">{{sws.time}}</td>
                #     {% else %}
                #         {% if sws.time < ws.time %}
                #             <td width="20px">{{sws.time}}</td>
                #         {% else %}
                #             <td width="20px">{{sws.time}}</td>
                #         {% endif %}
                #     {% endif %}
                # {% empty %}
                #     <td width="20px"></td>
                # {% endfor %}


# def songbyws(request, chorus_id):
#     song_table = {}
#     ws_row = WS.objects.filter(chorus_id=5).order_by('time')
#     song_list = Song.objects.filter(hymnal_id=23)
#     for song in song_list:
#         song_row = SongvsWS.objects.filter(song_id = song.id).order_by('ws__time')
#         song_table[unicode(song.Name)] = song_row
#         ws_min =
#     context = {'song_table':song_table, 'ws_row' : ws_row, 'tdcolor':'lightblue'}
#     return render(request, 'hymnals/songbyws.html', context)


# <td>{{ song }}</td>
#             {% for sws in songrow %}
#                 {% for ws in ws_row %}
#                     {% if sws.time != ws.time %}
#                         {% if sws.time > ws.time %}
#                             <td width="20px">{{sws.time}}</td>
#                         {% endif %}
#                     {% else %}
#                         {% if sws.ws_id == ws.id %}
#                             <td width="20px" bgcolor="{{tdcolor}}">{{sws.time}}</td>
#                         {% endif %}
#                     {% endif %}
#                 {% endfor %}
#             {% empty %} <!-- empty ws row - fill it -->
#                 {% for ws in ws_row %}
#                     <td width="20px"></td>
#                 {% endfor %}
#             {% endfor %}