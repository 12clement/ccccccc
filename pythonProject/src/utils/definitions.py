mandatory_column_value_list = [
    'payload_policyDetails_risks_proposer_postalAddress_UDPRN',
    'payload_policyDetails_risks_proposer_postalAddress_postcode',
    'payload_policyDetails_risks_proposer_postalAddress_townCity',
    'payload_policyDetails_risks_coverType',
    'payload_policyDetails_fees_status',
    'payload_policyDetails_tenant_brandId',
    'payload_policyDetails_tenant_productId',
    'payload_policyDetails_quoteControl_system_brokerNumber',
    'payload_policyDetails_quoteControl_system_schemeIdentifier',
    'payload_policyDetails_quoteControl_document_policyClassType',
    'payload_policyDetails_quoteControl_document_transactionType',
    'payload_policyDetails_risks_proposer_communications_method',
    'payload_policyPremium_payments_externalReferences_referenceName',
    'payload_policyPremium_payments_externalReferences_referenceValue'
    #,'payload_policyDetails_risks_motorRisk_vehicleOwnership_vehicle_vehicleReference'
   ]


payment_plan_mandatory_column_value_list = [
'payload_paymentPlan_paymentPlanModel_tenant_brandId'
,'payload_paymentPlan_paymentPlanModel_tenant_productId'
,'eventId'
,'payload_paymentPlan_instalments_instalmentHistory_metadata_createdAt'
,'payload_paymentPlan_instalments_instalmentHistory_metadata_createdBy'
,'payload_paymentPlan_noticePeriod'
,'payload_paymentPlan_planHistory_externalReferences_referenceName'
,'payload_paymentPlan_planHistory_externalReferences_referenceValue'
,'payload_paymentPlan_externalReferences_referenceName'
,'payload_paymentPlan_externalReferences_referenceValue'
,'payload_paymentPlan_metadata_createdBy'
    ]

payment_plan_changed_mandatory_column_value_list = [
'payload_paymentPlan_paymentPlanModel_tenant_brandId'
,'payload_paymentPlan_paymentPlanModel_tenant_productId'
,'eventId'
,'payload_paymentPlan_instalments_instalmentHistory_metadata_createdAt'
,'payload_paymentPlan_instalments_instalmentHistory_metadata_createdBy'
,'payload_paymentPlan_noticePeriod'
,'payload_paymentPlan_planHistory_externalReferences_referenceName'
,'payload_paymentPlan_planHistory_externalReferences_referenceValue'
,'payload_paymentPlan_externalReferences_referenceName'
,'payload_paymentPlan_externalReferences_referenceValue'
,'payload_paymentPlan_metadata_createdBy'
    ]

external_refund_created_mandatory_column_value_list = [
'payload_transactionDate'
,'payload_reason'
,'eventId'
,'payload_metadata_createdAt'
,'payload_metadata_createdBy'
,'payload_externalReferences_referenceName'
,'payload_externalReferences_referenceValue'
    ]


card_refund_processed_mandatory_column_value_list = [
'payload_contact_postalAddress_UDPRN'
,'payload_contact_postalAddress_townCity'
,'payload_contact_postalAddress_postcode'
,'payload_externalReferences_referenceName'
,'payload_externalReferences_referenceValue'
,'payload_metadata_createdAt'
,'payload_metadata_createdBy'
,'payload_paymentReference'
,'payload_reason'
,'payload_transactionDate'
    ]

card_operation_refund_processed_mandatory_column_value_list = [
'payload_externalReferences_referenceName'
,'payload_externalReferences_referenceValue'
,'payload_metadata_createdAt'
,'payload_metadata_createdBy'
,'payload_paymentReference'
,'payload_reason'
,'payload_transactionDate'
    ]

payment_instalment_changed_mandatory_column_value_list = [
'payload_instalment_instalmenthistory_accountname'
,'payload_instalment_instalmenthistory_accountnumber'
,'payload_instalment_instalmenthistory_duedate'
,'payload_instalment_instalmenthistory_metadata_createdat'
,'payload_instalment_instalmenthistory_metadata_createdby'
,'payload_instalment_instalmenthistory_instalmentnumber'
,'payload_instalment_metadata_createdat'
,'payload_instalment_metadata_createdby'
    ]

payment_ext_payment_created_mandatory_column_value_list = [
'payload_externalreferences_referencename'
,'payload_externalreferences_referencevalue'
,'payload_metadata_createdat'
,'payload_metadata_createdby'
,'eventid'
    ]

payment_directcredit_created_mandatory_column_value_list = [
'eventid'
,'payload_directcredit_directcredithistory_accountname'
,'payload_directcredit_directcredithistory_accountnumber'
,'payload_directcredit_directcredithistory_externalreferences_referencename'
,'payload_directcredit_directcredithistory_externalreferences_referencevalue'
,'payload_directcredit_directcredithistory_metadata_createdat'
,'payload_directcredit_directcredithistory_metadata_createdby'
,'payload_directcredit_tenant_brandid'
,'payload_directcredit_tenant_productid'
    ]

payment_directcredit_changed_mandatory_column_value_list = [
'eventid'
,'payload_directcredit_directcredithistory_accountname'
,'payload_directcredit_directcredithistory_accountnumber'
,'payload_directcredit_directcredithistory_externalreferences_referencename'
,'payload_directcredit_directcredithistory_externalreferences_referencevalue'
,'payload_directcredit_directcredithistory_metadata_createdat'
,'payload_directcredit_directcredithistory_metadata_createdby'
,'payload_directcredit_tenant_brandid'
,'payload_directcredit_tenant_productid'
    ]


payment_bankdetails_created_mandatory_column_value_list = [
'eventid'
#,'payload_bankdetails_bankdetailshistory_externalreferences'
,'payload_bankdetails_bankdetailshistory_metadata_createdat'
,'payload_bankdetails_tenant_brandid'
,'payload_bankdetails_tenant_productid'
,'payload_bankdetails_planid'
]

payment_bankdetails_changed_mandatory_column_value_list = [
'eventid'
,'payload_bankdetails_externalreferences_referencename'
,'payload_bankdetails_externalreferences_referencevalue'
,'payload_bankdetails_tenant_brandid'
,'payload_bankdetails_tenant_productid'
,'payload_bankdetails_planid'
]

payment_writeoff_balance_created_mandatory_column_value_list = [
'eventid'
,'payload_externalreferences_referencename'
,'payload_externalreferences_referencevalue'
,'payload_reason_code'
,'payload_writeoffoption'
,'payload_metadata_createdat'
,'payload_reason_description'
]


payment_admin_pymnt_credit_created_mandatory_column_value_list = [
'eventid'
,'payload_externalreferences_referencename'
,'payload_externalreferences_referencevalue'
,'payload_metadata_createdat'
,'payload_reason_code'
,'payload_reason_description'
,'payload_metadata_createdby'
]


payment_admin_pymnt_credit_changed_mandatory_column_value_list = [
'eventid'
,'payload_externalreferences_referencename'
,'payload_externalreferences_referencevalue'
,'payload_metadata_createdat'
,'payload_reason_code'
,'payload_reason_description'
,'payload_metadata_createdby'
]

card_payment_processed_mandatory_column_value_list = [
'payload_card_last4'
,'eventId'
,'payload_externalreferences_referencename'
,'payload_externalreferences_referencevalue'
,'payload_metadata_createdat'
,'payload_metadata_createdby'
,'payload_paymentmethod'
,'payload_paymentreference'
    ]


