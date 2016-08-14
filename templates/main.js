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
var values = [];
var del_val = [];
$scope.options =[];

console.log('{{login}}');
{%if login == "true" %}
  var myEl = angular.element( document.querySelector( '#Login-session' ) );
  $scope.second_form = true;
  myEl.remove();
{% endif %}

$scope.city_toggle = function(selectedItem){

if(selectedItem){
  $scope.menu = true;


}


};

$scope.Menu_toggle = function(selectedmenu,add){
if( ! add){

  $scope.options =[]
}

if(selectedmenu){
  $scope.edit = true;

  console.log(selectedmenu)
}
switch (selectedmenu) {
  case "Event":
  $scope.options.push ({name:'Name'},{name:'Date'},{name:'Rating'}, {name: 'Address'});
  break;

  case "Places":
  $scope.options.push ({name:'Name'},{name:'Rating'},{name:'Details'}, {name: 'Address'});
  break;

  case "Hotels":
  $scope.options.push ({name:'Name'},{name:'Rating'},{name:'Type'}, {name: 'Address'});
  break;

  case "Resturants":
  $scope.options.push ({name:'Name'},{name:'Rating'},{name:'Cuisine'}, {name: 'Address'});
  break;


}



};
$scope.del_func= function(selectedItem, selectedmenu, options){
del_val.push(options)
console.log(values);
$http.post('/details', { 'uid': [del_val, selectedItem , selectedmenu,1]}).success(function(response) {



});
$scope.edit = false;
$scope.options= [];
del_val = [];


}

$scope.edit_func = function(selectedItem, selectedmenu, options){

values.push(options);
console.log(values);



$http.post('/details', { 'uid': [values, selectedItem , selectedmenu,0]}).success(function(response) {



});
$scope.edit = false;
$scope.options= [];


};

$scope.Add_func = function(){

$scope.options.push({})



};


});
