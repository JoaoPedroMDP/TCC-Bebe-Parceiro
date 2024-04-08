import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DeleteBeneficiaryComponent } from './delete-beneficiary.component';

describe('DeleteBeneficiaryComponent', () => {
  let component: DeleteBeneficiaryComponent;
  let fixture: ComponentFixture<DeleteBeneficiaryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DeleteBeneficiaryComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DeleteBeneficiaryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
