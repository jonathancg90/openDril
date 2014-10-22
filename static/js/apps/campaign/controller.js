
function campaignCtrl($scope, requestService, factoryUrl, contextData) {

    var url_filter_details = factoryUrl.campaignFilterListDetail,
        url_save_filter_detail = factoryUrl.saveCampaignListDetail,
        url_delete_filter_detail = factoryUrl.deleteCampaignListDetail;

    $scope.categories = [];
    $scope.lists = JSON.parse(contextData.lists);

    $scope.getDetailFilter = function(campaign_id){
        $scope.newCampaign = campaign_id;
        var url = url_filter_details.replace("campaign_pk", campaign_id);
        var detail_filter_response = requestService.get(url);

        detail_filter_response.success(function(res) {
            $scope.detail_filter = res;
        });
    };

    $scope.getCategories = function(){
        $scope.newCategory = undefined;
        $scope.categories = $scope.newList.list_categories;
    };

    $scope.deleteDetail = function(idx, campaign_id) {
        var data = {
            'detail_id': campaign_id
        };
        var response = requestService.post(url_delete_filter_detail, data);

        response.success(function(res) {
            if(res.status == 'success'){
                $scope.detail_filter.splice(idx, 1);
            }
        });
    };

    $scope.addDetail = function(){
        var category = undefined;
        if($scope.newCategory !=undefined){
            category = $scope.newCategory.category_id
        }

        var data = {
            'campaign': $scope.newCampaign,
            'list': $scope.newList.list_id,
            'category': category
        };

        var response = requestService.post(url_save_filter_detail, data);

        response.success(function(res) {
            if(res.status == 'success') {
                $scope.detail_filter.push(res.data);
            }
        });
    };

}

angular
    .module('campaignApp')
    .controller('campaignCtrl', campaignCtrl);