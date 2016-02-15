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
