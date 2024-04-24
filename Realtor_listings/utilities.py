import datetime
from datetime import timedelta

req_headers = {
                "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                'accept':' application/json',
                "accept-encoding": "gzip, deflate, br",
                "content-type": "application/json"
            }


def property_query(property_id_is):
    
    query = {
   "query":"{\n    home(property_id: \"%s\") {\n      advertisers {\n        team_name\n        address {\n          city\n          country\n          line\n          postal_code\n          state\n          state_code\n        }\n        builder {\n          fulfillment_id\n        }\n        broker {\n          accent_color\n          designations\n          fulfillment_id\n          name\n          logo\n        }\n        email\n        fulfillment_id\n        href\n        mls_set\n        name\n        nrds_id\n        office {\n          address {\n            city\n            coordinate {\n              lat\n              lon\n            }\n            country\n            line\n            postal_code\n            state\n            state_code\n          }\n          application_url\n          email\n          lead_email {\n            to\n            cc\n          }\n          fulfillment_id\n          hours\n          href\n          mls_set\n          out_of_community\n          name\n          phones {\n            ext\n            number\n            primary\n            trackable\n            type\n          }\n          photo {\n            href\n          }\n          slogan\n        }\n        phones {\n          ext\n          number\n          primary\n          trackable\n          type\n        }\n        photo {\n          href\n        }\n        slogan\n        type\n      }\n      buyers {\n        address {\n          city\n          country\n          line\n          postal_code\n          state\n          state_code\n        }\n        broker {\n          accent_color\n          designations\n          fulfillment_id\n          name\n          logo\n        }\n        email\n        fulfillment_id\n        href\n        mls_set\n        name\n        nrds_id\n        office {\n          address {\n            city\n            coordinate {\n              lat\n              lon\n            }\n            country\n            line\n            postal_code\n            state\n            state_code\n          }\n          application_url\n          email\n          lead_email {\n            to\n            cc\n          }\n          fulfillment_id\n          hours\n          href\n          mls_set\n          out_of_community\n          name\n          phones {\n            ext\n            number\n            primary\n            trackable\n            type\n          }\n          photo {\n            href\n          }\n          slogan\n        }\n        phones {\n          ext\n          number\n          primary\n          trackable\n          type\n        }\n        photo {\n          href\n        }\n        slogan\n        type\n      }\n      community {\n        permalink\n      }\n      estimates {\n        current_values(source: \"corelogic\")\n        @include_if(field: \"status\", operator: in, value: \"sold,off_market,other\") {\n          estimate\n          estimate_high\n          estimate_low\n          date\n          source {\n            type\n            name\n          }\n        }\n      }\n      days_on_market\n      description {\n        baths\n        baths_3qtr\n        baths_full\n        baths_full_calc\n        baths_half\n        baths_max\n        baths_min\n        baths_partial_calc\n        baths_total\n        beds\n        beds_max\n        beds_min\n        construction\n        cooling\n        exterior\n        fireplace\n        garage\n        garage_max\n        garage_min\n        garage_type\n        heating\n        logo {\n          href\n        }\n        lot_sqft\n        name\n        pool\n        roofing\n        rooms\n        sqft\n        sqft_max\n        sqft_min\n        stories\n        styles\n        sub_type\n        text\n        type\n        units\n        year_built\n        year_renovated\n        zoning\n      }\n      details {\n        category\n        parent_category\n        text\n      }\n      flags {\n        is_coming_soon\n        is_contingent\n        is_deal_available\n        is_for_rent\n        is_foreclosure\n        is_garage_present\n        is_new_construction\n        is_pending\n        is_price_excludes_land\n        is_senior_community\n        is_short_sale\n        is_subdivision\n      }\n      href\n      last_sold_date\n      last_sold_price\n      list_date\n      list_price\n      listing_id\n      local {\n        flood {\n          firststreet_url\n          fsid\n          flood_factor_score\n          flood_factor_severity\n          environmental_risk\n          trend_direction\n          fema_zone\n          insurance_requirement\n          insurance_quotes{\n            provider_url\n            provider_name\n            provider_logo\n            expires\n            price\n            home_coverage\n            contents_coverage\n            disclaimer\n          }\n        }\n        noise {\n          score\n        }\n      }\n      location {\n        address {\n          city\n          coordinate {\n            lat\n            lon\n          }\n          country\n          line\n          postal_code\n          state\n          state_code\n          street_direction\n          street_name\n          street_number\n          street_post_direction\n          street_suffix\n          unit\n          validation_code\n        }\n        county {\n          fips_code\n          name\n          state_code\n        }\n        neighborhoods {\n          city\n          id\n          level\n          name\n          state_code\n          slug_id\n        }\n        search_areas {\n          city\n          state_code\n        }\n        city {\n          county_needed_for_uniq\n        }\n      }\n      nearby_schools {\n        schools {\n          coordinate {\n            lat\n            lon\n          }\n          distance_in_miles\n          district {\n            id\n            name\n          }\n          education_levels\n          funding_type\n          grades\n          greatschools_id\n          id\n          name\n          nces_code\n          parent_rating\n          rating\n          review_count\n          slug_id\n          student_count\n        }\n      }\n      photo_count\n      photos {\n        title\n        description\n        href\n        type\n      }\n      primary_photo {\n        href\n      }\n      property_history {\n        date\n        event_name\n        price\n        price_sqft\n        source_listing_id\n        source_name\n        listing @include_if(field: \"status\", operator: in, value: \"sold,off_market,other\") {\n          list_price\n          last_status_change_date\n          last_update_date\n          status\n          list_date\n          listing_id\n          suppression_flags\n          photos {\n            href\n          }\n          description {\n            text\n          }\n          advertisers {\n            fulfillment_id\n            nrds_id\n            name\n            email\n            href\n            slogan\n            office {\n              fulfillment_id\n              name\n              email\n              href\n              slogan\n              out_of_community\n              application_url\n              mls_set\n            }\n            broker {\n              fulfillment_id\n              name\n              accent_color\n              logo\n            }\n            type\n            mls_set\n          }\n          buyers {\n            fulfillment_id\n            nrds_id\n            name\n            email\n            href\n            slogan\n            type\n            mls_set\n            address {\n              line\n              city\n              postal_code\n              state_code\n              state\n              country\n              coordinate {\n                lat\n                lon\n              }\n            }\n            office {\n              fulfillment_id\n              name\n              email\n              href\n              slogan\n              hours\n              out_of_community\n              application_url\n              mls_set\n              address {\n                line\n                city\n                postal_code\n                state_code\n                state\n                country\n              }\n              phones {\n                number\n                type\n                primary\n                trackable\n                ext\n              }\n              county {\n                name\n              }\n            }\n            phones {\n              number\n              type\n              primary\n              trackable\n              ext\n            }\n            broker {\n              fulfillment_id\n              name\n              accent_color\n              logo\n            }\n          }\n          source {\n            id\n            agents {\n              agent_id\n              agent_name\n              office_id\n              office_name\n              office_phone\n              type\n            }\n          }\n        }\n      }\n      property_id\n      provider_url {\n        href\n        level\n        type\n      }\n      source {\n        agents {\n          agent_id\n          agent_name\n          id\n          office_id\n          office_name\n          office_phone\n          type\n        }\n        disclaimer {\n          href\n          logo {\n            href\n            height\n            width\n          }\n          text\n        }\n        id\n        plan_id\n        listing_id\n        name\n        raw {\n          status\n          style\n          tax_amount\n        }\n        type\n        community_id\n      }\n      status\n      suppression_flags\n      tags\n      tax_history {\n        assessment {\n          building\n          land\n          total\n        }\n     \
          market {\n          building\n          land\n          total\n        }\n        tax\n        year\n      }\n    }\n  }"%(property_id_is),
   "variables":{
      
   },
   "callfrom":"PDP",
   "isClient":True
                    }
    return query




def sold_listing_query(location, page_num, offset, state_code):
    # Query for current week sold properties
    current_week= datetime.date.today() - timedelta(days=7)
    
    query = {
                "query":"\n\nquery ConsumerSearchMainQuery($query: HomeSearchCriteria!, $limit: Int, $offset: Int, $sort: [SearchAPISort], $sort_type: SearchSortType, $client_data: JSON, $bucket: SearchAPIBucket)\n{\n  home_search: home_search(query: $query,\n    sort: $sort,\n    limit: $limit,\n    offset: $offset,\n    sort_type: $sort_type,\n    client_data: $client_data,\n    bucket: $bucket,\n  ){\n    count\n    total\n    results {\n      property_id\n      list_price\n      primary_photo (https: true){\n        href\n      }\n      source {\n        id\n        agents{\n          office_name\n        }\n        type\n        spec_id\n        plan_id\n      }\n      community {\n        property_id\n        description {\n          name\n        }\n        advertisers{\n          office{\n            hours\n            phones {\n              type\n              number\n            }\n          }\n          builder {\n            fulfillment_id\n          }\n        }\n      }\n      products {\n        brand_name\n        products\n      }\n      listing_id\n      matterport\n      virtual_tours{\n        href\n        type\n      }\n      status\n      permalink\n      price_reduced_amount\n      other_listings{rdc {\n      listing_id\n      status\n      listing_key\n      primary\n    }}\n      description{\n        beds\n        baths\n        baths_full\n        baths_half\n        baths_1qtr\n        baths_3qtr\n        garage\n        stories\n        type\n        sub_type\n        lot_sqft\n        sqft\n        year_built\n        sold_price\n        sold_date\n        name\n      }\n      location{\n        street_view_url\n        address{\n          line\n          postal_code\n          state\n          state_code\n          city\n          coordinate {\n            lat\n            lon\n          }\n        }\n        county {\n          name\n          fips_code\n        }\n      }\n      tax_record {\n        public_record_id\n      }\n      lead_attributes {\n        show_contact_an_agent\n        opcity_lead_attributes {\n          cashback_enabled\n          flip_the_market_enabled\n        }\n        lead_type\n      }\n      open_houses {\n        start_date\n        end_date\n        description\n        methods\n        time_zone\n        dst\n      }\n      flags{\n        is_coming_soon\n        is_pending\n        is_foreclosure\n        is_contingent\n        is_new_construction\n        is_new_listing (days: 14)\n        is_price_reduced (days: 30)\n        is_plan\n        is_subdivision\n      }\n      list_date\n      last_update_date\n      coming_soon_date\n      photos(limit: 2, https: true){\n        href\n      }\n      tags\n      branding {\n        type\n        photo\n        name\n      }\n    }\n  }\n}",
                "variables":{
                    "query":{
                        "sold_price":{
                            "min":750000
                        },
                        "status":[
                            "sold"
                        ],
                        "sold_date":{
                            "min":f"{current_week}T17:22:30.359Z"               
                        },
                        "state_code":"%s"%(state_code)
                    },
                    "client_data":{
                        "device_data":{
                            "device_type":"web"
                        },
                        "user_data":{
                            "last_view_timestamp":-1
                        }
                    },
                    "limit":42,
                    "offset":offset,
                    "zohoQuery":{
                        "silo":"search_result_page",
                        "location":"%s"%(location),
                        "property_status":"for_sale",
                        "filters":{
                            "price":{
                            "min":750000
                            },
                            "show_listings":[
                            "rs"
                            ],
                            "radius":None
                        },
                        "page_index":"%s"%(page_num)
                    },
                    "geoSupportedSlug":"",
                    "resetMap":f"{str(datetime.date.today())}",
                    "sort":[
                        {
                            "field":"sold_date",
                            "direction":"desc"
                        },
                        {
                            "field":"photo_count",
                            "direction":"desc"
                        }
                    ],
                    "by_prop_type":[
                        "home"
                    ]
                },
                "operationName":"ConsumerSearchMainQuery",
                "callfrom":"SRP",
                "nrQueryType":"MAIN_SRP",
                "visitor_id":"1df8bb84-5a01-42b5-9620-575b54fabfba",
                "isClient":True,
                "seoPayload":{
                    "asPath":"/realestateandhomes-search/%s/price-750000-na/show-recently-sold/pg-%s"%(location.replace(" ","-"), page_num),
                    "pageType":{
                        "silo":"search_result_page",
                        "status":"for_sale"
                    },
                    "county_needed_for_uniq":False
                }
                }
    return query
