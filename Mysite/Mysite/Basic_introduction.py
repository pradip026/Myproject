from django.http import HttpResponse
def simple(request):
    return HttpResponse("<p>Hello DO you want to Know What is Python</p><a href=https://learn.edx.org/topic-python/?g_acctid=926-195-8061&g_campaign=gs-free-nonbrand-subject-python&g_campaignid=896085961&g_adgroupid=46573740945&g_adid=282235687824&g_keyword=program%"
                        "20in%20python&g_keywordid=kwd-305697475372&g_network=g?utm_source=adwords&utm_campaign=896085961&utm_medium=46573740945&utm_term=program%20in%20python&gclid=CjwKCAjwk93rBRBLEiwAcMapUcWLKWR449BDiqonpYkfl_slZcHwq5lZDiYEYSALx2zNKCAYncXzhBoC0BAQAvD_BwE>"
                        "Click Here</a>")
def login(request):
    return HttpResponse('''<center><table>
    <form>
    <th>Login Form</th>
    <tr>
        <td>First Name</td>
        <td><input type='text'></td>
    </tr>
    <tr>
        <td>Last Name</td>
        <td><input type='text'></td>
    </tr>
    <tr>
        <td>password</td>
        <td><input type='password'></td>
    </tr>
    <tr>
        <td>Gender</td>
        <td><input type='radio' name='Gender'value='Male'>Male</td>
        <td><input type='radio' name='Gender'value='Female'>Female</td>
    </tr>
    <tr> </tr>
    <tr> </tr>
    <tr><td><input type='button' value='submit'></td>
    <td><input type='button' value='clear'></td>
    <td>
    <a href='/'>Back</a>
    </td></tr>
    
    </form>
    </table></center>''')