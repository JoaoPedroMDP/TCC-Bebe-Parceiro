import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListBeneficiaryComponent } from './list-beneficiary.component';

describe('ListBeneficiaryComponent', () => {
  let component: ListBeneficiaryComponent;
  let fixture: ComponentFixture<ListBeneficiaryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ListBeneficiaryComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ListBeneficiaryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
