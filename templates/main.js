var app = angular.module("myApp", []);
app.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{a');
  $interpolateProvider.endSymbol('a}');
}]);

app.controller("myCtrl", function($scope, $rootScope) {

  $scope.toggleSibling = function($event){

    console.log($event.target.id);
    if ($event.target.id == "events"){
      $scope.select_value = true;
      $scope.filters = {"value":" "};
      $rootScope.filter_value = false ;
      $scope.even = [];

      $scope.names = ["Date", "-Popular"];



      {%for events in city_value['City_events']%}
        $scope.even.push({'Name':'{{events[0]}}', 'Date':'{{events[1]}}','Popular':'{{events[2]}}','Address':'{{events[3]}}'} ); // Gets the event name
      {% endfor %}



    console.log($scope.even);


  }
  if ($event.target.id == "Places"){
    $scope.even = [];
    $scope.names = ["-Popular"];
    $scope.select_value = true;
    $scope.filters = {"value":" "};
    $rootScope.filter_value = false ;
    {%for events in city_value['City_places']%}
      $scope.even.push({'Name':'{{events[0]}}', 'Popular':'{{events[1]}}','Date':'{{events[2]}}','Address':'{{events[3]}}'} ); // Gets the event name
    {% endfor %}
  console.log($scope.even);

}
if ($event.target.id == "Hotels"){
  $scope.even = [];
  $scope.names = ["-Popular","-Type"];
  $scope.select_value = true;
  $scope.filters = {"value":" "};
  $rootScope.filter_value = false ;
  {%for events in city_value['City_hotels']%}
$scope.even.push({'Name':'{{events[0]}}', 'Popular':'{{events[1]}}','Type':'{{events[2]}}','Address':'{{events[3]}}'} );
{% endfor %}

}
if ($event.target.id == "resturants"){
$scope.even = [];
$scope.names = ["-Popular","Type"];
$scope.filters = {
                  "value":"American",
                  "values": ["American", "Indian", "Chinese", "Italian","Thai"]}
$scope.select_value = true;
$rootScope.filter_value = true;


{%for events in city_value['City_resturants']%}
  $scope.even.push({'Name':'{{events[0]}}', 'Popular':'{{events[1]}}','Type':'{{events[2]}}','Address':'{{events[3]}}'} );
{% endfor %}


}
}

$scope.style_func = function(){
  {% if city_value['City_name'] == 'San Francisco'%}
    var style1 = "background-image: url(../static/gg.jpg); background-size: cover;";
    return style1;
  {%endif %}
  {% if city_value['City_name'] == 'San Jose'%}
    var style1 = "background-image: url(../static/sj.jpg); background-size: cover;";
    return style1;
  {%endif %}
  {% if city_value['City_name'] == 'San Diego'%}
    var style1 = "background-image: url(../static/sd.jpg); background-size: cover;";
    return style1;
  {%endif %}
  {% if city_value['City_name'] == 'Los Angeles'%}
    var style1 = "background-image: url(../static/la.jpg); background-size: cover;";
    return style1;
  {%endif %}

}
});
