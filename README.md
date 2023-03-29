<h1>Twittify API</h1>
<p>This is a simple web app that offers a few endpoints that
connect with Twitter API, do various things with acquired data
and return a result. You can for example check, what is the most 
liked Tweet by a certain user, which is not something you can 
do with standard twitter API.</p>

<h2>Endpoints</h2>
<table>
  <thead>
    <tr>
      <th>endpoint</th>
      <th>request</th>
      <th>response</th>
      <th>params</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/tweets/sentiment/[user_id]</td>
      <td>GET</td>
      <td>Simple JSON object saying whether the tweets of given user are positive</td>
      <td>None</td>
    </tr>
    <tr>
      <td>/tweets/freq_langs</td>
      <td>GET</td>
      <td>Returns a dictionary with key value pairs corresponding to programming_language: number_of_occurences, in latest 100 tweets </td>
    <td>None</td>
    </tr>
    <tr>
      <td>/tweets/most_popular/[user_id]</td>
      <td>GET</td>
      <td>Returns most popular tweets for specified user. By default 100, use a num_tweets param to change that number.</td>
<td>num_tweets</td>
    </tr>

  </tbody>
</table>
